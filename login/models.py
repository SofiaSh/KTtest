from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .user_manager import UserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to='images/', blank=True, verbose_name='аватар')
    patronymic = models.CharField(verbose_name='отчество', max_length=40, default=' ')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    

    class Meta:
        db_table = 'User'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
