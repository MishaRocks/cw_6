from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView

from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView

from users.forms import LoginForm, UserProfileForm, UserRegForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/user_login.html'
    form_class = LoginForm


class LogoutView(BaseLogoutView):
    ...


class RegisterView(CreateView):
    model = User
    form_class = UserRegForm
    template_name = 'users/user_registration.html'
    success_url = reverse_lazy('users:registration_success')

    def form_valid(self, form):
        new_user = form.save()
        verification_url = self._generate_verification_url(new_user.pk)
        send_mail(
            subject='Подтвердите ваш адрес электронной почты',
            message=f'Пожалуйста нажмите на следующую ссылку, чтобы подтвердить свой адрес электронной почты: '
                    f'{ verification_url }',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

    def _generate_verification_url(self, user_pk):
        return self.request.build_absolute_uri(
            reverse('users:verification', kwargs={'pk': user_pk}))


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/user_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verification_view(request, pk):
    user = get_object_or_404(User, pk=pk)

    if not user.is_email_verified:
        user.is_email_verified = True
        user.save()

    return redirect('users:login')


def registration_success(request):
    return render(request, template_name='users/email_verification.html')
