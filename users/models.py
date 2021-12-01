from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.base import Model
from django.utils.translation import gettext_lazy
from company.models import Deal

# Create your models here.



GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, mobile, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            mobile=mobile,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # 
    name = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField( choices=GENDER_CHOICES, max_length=50,blank=True,null=True)
    mobile = models.CharField(max_length=12,unique=True)
    mobile_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4,blank=True,null=True)
    country = models.CharField(max_length=100)
    # 

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


