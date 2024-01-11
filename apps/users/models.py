from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str = None,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> "User":
        if not email:
            raise ValueError(_("User must have an email"))
        if not first_name:
            raise ValueError(_("User must have a first name"))
        if not last_name:
            raise ValueError(_("User must have a last name"))

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name=_("First name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last name"))
    email = models.EmailField(max_length=100, verbose_name=_("Email"), unique=True)
    username = None
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# modelo de usuario productor
class UserProducer(User):
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    birthdate = models.DateField(verbose_name=_("Birthdate"))
    dni = models.CharField(max_length=10, verbose_name=_("DNI"), unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# modelo de usuario cliente
class UserClient(User):
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    dni = models.CharField(max_length=10, verbose_name=_("DNI"), unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
