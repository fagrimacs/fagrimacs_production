from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('You must have an Email Address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=100, verbose_name='Full name')
    phone = PhoneNumberField(verbose_name='Phone Number',
                             help_text='+255 xxx xxx xxx')
    ABOUT_US = [
        (None, 'Please Select'),
        ('Whatsapp status', 'Whatsapp status'),
        ('Internet search', 'Internet Search'),
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Twitter', 'twitter'),
        ('Linkedln', 'Linkedln'),
        ('Industry Conference', 'Industry Conference'),
        ('Industry Publication', 'Industry Publication'),
        ('Fagrimacs publications', 'Fagrimacs publications'),
        ('Word of mouth', 'Word of mouth'),
        ('Other', 'Other'),
    ]
    hear_about_us = models.CharField(
        max_length=150, verbose_name='How did you hear about us?',
        choices=ABOUT_US)
    is_active = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

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
        return self.is_superuser
