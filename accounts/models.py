from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Users(models.Model):
    """Модель содержит список пользователей сайта"""
    user = models.OneToOneField(User, verbose_name='Профиль пользователя', on_delete=models.CASCADE)
    date_birth = models.DateField("Дата рождения", blank=True, null=True)
    status = models.CharField("Статус", max_length=140, blank=True, null=True)
    bio = models.TextField("Информация о себе", blank=True, null=True)

    def __str__(self) -> str:
        return '{}'.format(self.user)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Users.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.users.save()
