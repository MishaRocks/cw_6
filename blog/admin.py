from django.contrib import admin

# Register your models here.
from blog.models import Blogpost


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'views_count', 'date_published',)
