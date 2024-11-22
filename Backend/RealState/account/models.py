from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import Permission
from django.core.validators import RegexValidator

''' nepali number validations'''
nepali_mobile_regex = RegexValidator(
    regex=r'^(98|97)\d{8}$',
    message="Only 10 digits NTC or NCELL numbers allowed."
)


'''Custom User Manager'''
class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None ,last_name=None, phone_no=None, password=None, password2=None,**extra_fields):
        
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_no= phone_no
        )

        user.set_password(password)
        user.is_user = True
        user.save(using=self._db)
        # view_product_permission = Permission.objects.get(codename='view_product')
        # user.user_permissions.add(view_product_permission)

        return user

    def create_superuser(self, email,name=None, phone_no=None, password=None,**extra_fields):
        user = self.create_user(
            email,
            password=password,
            name=name,
            phone_no= phone_no
        )
        user.is_admin = True
        user.is_superuser =True
        user.save(using=self._db)
        return user


'''Custom User Model'''
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=200,null=True, blank=True)
    last_name = models.CharField(max_length=200,null=True, blank=True)
    phone_no = models.CharField(validators=[nepali_mobile_regex], max_length=10,null=True, blank=True)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True) 

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name if self.first_name else self.email }"
    

    @property
    def is_staff(self):
        return self.is_admin +self.is_user


    def get_full_name(self):
        return self.first_name +self.last_name

