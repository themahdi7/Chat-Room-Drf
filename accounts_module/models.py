from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name=_('username'),
        max_length=40,
        unique=True,
    )
    nickname = models.CharField(verbose_name=_('nickname'), max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to="images/avatars", blank=True, null=True, verbose_name=_('avatar'))
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
