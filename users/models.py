from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from api.models import Startup, Investor


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, is_verified, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        is_verified=False,
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, True, **extra_fields)
    return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)
    startup = models.OneToOneField(Startup, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_startup')
    investor = models.OneToOneField(Investor, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_investor')
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    
    def get_email(self):
        return self.email