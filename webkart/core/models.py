from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

from django.conf import settings

ADDRESS_CHOICES = (
    ('WORK', 'Work',),
    ('HOME', 'Home',),
    ('Other', 'Other',),
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise (ValueError("Email not provided"))
        user = self.model(
            email=self.normalize_email(email),
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class Product(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # image = models.ImageField()
    # category = models.ManyToManyField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.name + ' ' + self.product.name

class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    line_1 = models.CharField(max_length=255)
    line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    type = models.CharField(
        max_length=20,
        choices=ADDRESS_CHOICES,
        default='HOME'
    )

    def __str__(self):
        return self.name
    
