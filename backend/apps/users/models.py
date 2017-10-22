from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator
import six
from django.contrib.auth.models import UserManager


class MyUserManager(UserManager):
    def _create_user(self, job_num, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not job_num:
            raise ValueError('The given job_num must be set')
        email = self.normalize_email(email)
        user = self.model(job_num=job_num, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, job_num, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(job_num, email, password, **extra_fields)

    def create_superuser(self, job_num, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(job_num, email, password, **extra_fields)


# Create your models here.

class UserProfile(AbstractUser):
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(
        '用户名',
        max_length=150,
        help_text='请输入您的名字',
        validators=[username_validator],
        null=True, blank=True
    )
    job_num = models.CharField(max_length=30, unique=True, verbose_name="工号", help_text="请填写工号，型如：z18861")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="手机号")
    phone = models.CharField(null=True, blank=True, max_length=20, verbose_name="工位分机号")
    avatar = models.ImageField(upload_to="avatar", default="", verbose_name="头像")
    USERNAME_FIELD = 'job_num'
    objects = MyUserManager()

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.job_num, self.username)
