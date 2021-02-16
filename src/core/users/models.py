from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Main user manager
    """

    def create_user(self, full_name, email, phone=None, password=None):
        """
        Creates and saves a user with the given phone.
        """
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=email, full_name=full_name, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(email=email, password=password, full_name=None)
        user.full_name = "Administrator"
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    avatar = models.FileField(verbose_name='Фото', blank=True, null=True)
    full_name = models.CharField(max_length=555, blank=True, null=True)
    
    email = models.EmailField(max_length=50, db_index=True, unique=True,
                             blank=False, null=False,
                             verbose_name=_('email'))
    phone = models.CharField(max_length=50, 
                             blank=True, null=True,
                             verbose_name=_('phone'))
    
    last_active = models.DateTimeField(null=True, blank=True, default=None, verbose_name='Активность '
                                                                                         'пользователя')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return '{} {}'.format(self.email,self.full_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


