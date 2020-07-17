from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
import random
import string
from slugify import slugify


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("You must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


#custom user account model
class User_Account(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique = True)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    username = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email



#custom profile extending the user account
class Profile(models.Model):
    user = models.OneToOneField(User_Account, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    project_credits = models.IntegerField(null=True, blank=True,default=0)
    private_profile = models.BooleanField(default=False, null=False)
    consent_marketing_notifications = models.BooleanField(default=True, null=False)
    user_profile_url = models.SlugField(max_length=100, blank=True, null=True, unique = True) #the slug field for the public profile url
    user_bio = models.CharField(max_length=2000, blank=True, null=True) # PLEASE_NOTE That this field is NOT inherited from models

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): # the autogeneration of the slug for the challenge
        if not self.user_profile_url:
            self.user_profile_url = slugify(self.name+'-'+str(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=6)))
        super(Profile, self).save(*args, **kwargs)


class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  MIN_USER = 1
  FULL_USER = 2
  ADVISOR = 3
  SUPERVISOR = 4
  ADMIN = 5
  ROLE_CHOICES = (
      (MIN_USER, 'visitor'),
      (FULL_USER, 'user'),
      (ADVISOR, 'advisor'),
      (SUPERVISOR, 'supervisor'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()
