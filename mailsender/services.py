from django.core.mail import send_mail
from django.conf import settings

from crontab import CronTab

from logs.models import Logs
from mailsender.models import Mailing


def send_mailing(mailing_object: Mailing):
    emails = [client.email for client in mailing_object.recipients.all()]
    try:
        send_mail(
            subject=mailing_object.message.title,
            message=mailing_object.message.content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails,
        )
        status_attempt = 'success'
        answer_server = 'Email sent successfully'
    except Exception as e:
        status_attempt = 'error'
        answer_server = str(e)

    log = Logs.objects.create(
        status_attempt=status_attempt,
        answer_server=answer_server,
        mailing=mailing_object,
    )

    return log


def generate_cron_schedule(mailing):
    if mailing.frequency == 'daily':
        cron_schedule = f'{mailing.sending_time.hour} {mailing.sending_time.minute} * * *'
    elif mailing.frequency == 'weekly':
        cron_schedule = f'{mailing.sending_time.hour} {mailing.sending_time.minute} * * {mailing.sending_date.strftime("%u")}'
    elif mailing.frequency == 'monthly':
        cron_schedule = f'{mailing.sending_time.hour} {mailing.sending_time.minute} {mailing.sending_date.day} * *'
    else:
        raise ValueError("Invalid frequency")

    return cron_schedule


def update_cron_jobs_for_user(user):
    cron = CronTab(user=user.name)

    # Удалите старые задачи Cron
    cron.remove_all(comment='mailing')

    # Получите все активные рассылки
    mailings = Mailing.objects.filter(is_active=True)

    # Создайте задачи Cron на основе параметров рассылки
    for mailing in mailings:
        cron_schedule = generate_cron_schedule(mailing)
        command = f'python manage.py runjob mailing {mailing.id}'
        job = cron.new(command=command, comment=f'mailing_{mailing.id}')
        job.setall(cron_schedule)
        job.enable()

    cron.write()
