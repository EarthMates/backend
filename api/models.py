from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
import string
import random



#User class for email authentication

class User(AbstractBaseUser, PermissionsMixin):
    models.EmailField(max_length=254, unique=True, verbose_name=_('Email Address'))
    first_name = models.CharField(max_length=150, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last Name'))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_('Date Joined'), auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS =['first_name', 'last_name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def tokens(self):
        pass
# Create your models here.

class Startup(models.Model):
        # Those are the choises for the field stage
    PRE_SEED = "PS"
    SERIES_A ='SA'
    SERIES_B = 'SB'
    SERIES_C = 'SC'
    BRIDGE ='BG'
    STAGE_CHOICES = {
        PRE_SEED : "PS",
        SERIES_A :'SA',
        SERIES_B : 'SB',
        SERIES_C : 'SC',
        BRIDGE :'BG'
    }
    stage = models.CharField(
        max_length=2,
        choices=STAGE_CHOICES,
        default= PRE_SEED
    )
    # Those are the choises for the field industry
    FINANCE = 'FN'
    AGRICULTURE = 'AG'
    TECHNOLOGY = 'TE'
    MOBILITY = 'MO'
    INDUSTRY_CHOICES = {
        FINANCE : 'FN',
        AGRICULTURE : 'AG',
        TECHNOLOGY : 'TE',
        MOBILITY : 'MO'
    }
    industry = models.CharField(
        max_length=2, 
        choices=INDUSTRY_CHOICES,
        default=FINANCE
    )
    # Those are the choises for the field location
    RWANDA = 'RW'
    GHANA = 'GH'
    NIGERIA = 'NG'
    LOCATION_CHOICES = {
        RWANDA : 'RW',
        GHANA : 'GH',
        NIGERIA : 'NG'
    }
    location = models.CharField(
        max_length=2,
        choices=LOCATION_CHOICES,
        default= RWANDA
    )
    name = models.CharField(max_length=50)
    capital = models.DecimalField(max_digits=15,decimal_places=0)
    impact = models.DecimalField(max_digits=10, decimal_places=0)
    sdg = models.JSONField()
    values = models.JSONField()
    expertise = models.JSONField()
    matching = models.JSONField()
    strategy = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    starup_owner = models.ForeignKey(User, related_name="startups", on_delete=models.CASCADE)


# Coded by Ghela:
# The constants below are used to create the dictionaries for the choises and in the 
# form are seen like a widjet of options.
class Investor(models.Model):

    # Those are the choises for the field stage
    PRE_SEED = "PS"
    SERIES_A ='SA'
    SERIES_B = 'SB'
    SERIES_C = 'SC'
    BRIDGE ='BG'
    STAGE_CHOICES = {
        PRE_SEED : "PS",
        SERIES_A :'SA',
        SERIES_B : 'SB',
        SERIES_C : 'SC',
        BRIDGE :'BG'
    }
    stage = models.CharField(
        max_length=2,
        choices=STAGE_CHOICES,
        default= PRE_SEED
    )
    # Those are the choises for the field industry
    FINANCE = 'FN'
    AGRICULTURE = 'AG'
    TECHNOLOGY = 'TE'
    MOBILITY = 'MO'
    INDUSTRY_CHOICES = {
        FINANCE : 'FN',
        AGRICULTURE : 'AG',
        TECHNOLOGY : 'TE',
        MOBILITY : 'MO'
    }
    industry = models.CharField(
        max_length=2,  
        choices=INDUSTRY_CHOICES,
        default=FINANCE
    )
    # Those are the choises for the field location
    RWANDA = 'RW'
    GHANA = 'GH'
    NIGERIA = 'NG'
    LOCATION_CHOICES = {
        RWANDA : 'RW',
        GHANA : 'GH',
        NIGERIA : 'NG'
    }
    location = models.CharField(
        max_length=2,
        choices=LOCATION_CHOICES,
        default=RWANDA
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    capital = models.DecimalField(max_digits=15,decimal_places=0, default=0)
    impact = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    sdg = models.JSONField(default=str)
    values = models.JSONField(default=str)
    expertise = models.JSONField(default=str)
    strategy = models.JSONField(default=str)
    created_at = models.DateTimeField(auto_now_add=True)
    investor_owner = models.ForeignKey(User, related_name="investors", on_delete=models.CASCADE)







# Routines to check boundries of data:
# - name none
# - stage in ["Pre Seed", "Series A", "Series B", "Series C", "Bridge"]
# - industry in ["Finance", "Agricolture", "Technology", "Mobility"]
# - location in ["Rwanda", "Ghana", "Nigeria"]
# - 10000 <= capital required <= 100 M


# Investor model:
# - name
# - stage
# - industry
# - location

# Routines to check boundries of data:
# - name none
# - stage in ["Pre Seed", "Series A", "Series B", "Series C", "Bridge"]
# - industry in ["Finance", "Agricolture", "Technology", "Mobility"]
# - location in ["Rwanda", "Ghana", "Nigeria"]