from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
            self, email, first_name, phone, address, password=None,
            commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have a first name'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            phone=phone,
            address=address,
        )

        user.set_password(password)
        user.is_publisher = False
        user.is_translator = False
        user.is_active = True
        user.is_admin = False
        user.is_staff = False
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password, address, phone):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            address=address,
            phone=phone,
            commit=False,
        )
        user.is_staff = True
        user.is_admin = True
        user.user_type = 1
        user.save(using=self._db)
        return user

    def create_publisher(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_publisher = True
        user.is_active = True
        user.user_type = 2
        user.save(using=self._db)
        return user

    def create_translator(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_translator = True
        user.is_active = True
        user.user_type = 3
        user.save(using=self._db)
        return user

    def create_proof_reader(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_proof_reader = True
        user.is_active = True
        user.user_type = 4
        user.save(using=self._db)
        return user

    def create_designer(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_designer = True
        user.is_active = True
        user.user_type = 5
        user.save(using=self._db)
        return user

    def create_writer(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_writer = True
        user.is_active = True
        user.user_type = 6
        user.save(using=self._db)
        return user

    def create_printer(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_printer = True
        user.is_active = True
        user.user_type = 7
        user.save(using=self._db)
        return user

    def create_request_service(self, email, first_name, phone, address, password):
        """
        Creates and saves a Secondary Employee USer with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_request_service = True
        user.is_active = True
        user.user_type = 8
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(
        _('Address'), max_length=255, null=True, blank=True)
    is_admin = models.BooleanField(_('Admin'), default=False, help_text=_(
        'Designates whether this user should be treated as an Admin. '
    ))
    is_translator = models.BooleanField(_('translator'), default=False, help_text=_(
        'Designates whether this user should be treated as an Secondary Employee. '
    ))
    is_publisher = models.BooleanField(_('publisher'), default=False, help_text=_(
        'Designates whether this user should be treated as a publisher. '
    ))
    is_designer = models.BooleanField(_('Designer'), default=False, help_text=_(
        'Designates whether this user should be treated as a Designer. '
    ))
    is_writer = models.BooleanField(_('Writer'), default=False, help_text=_(
        'Designates whether this user should be treated as a Request Service. '
    ))
    is_request_service = models.BooleanField(_('Request Service'), default=False, help_text=_(
        'Designates whether this user should be treated as a Request Service. '
    ))
    is_proof_reader = models.BooleanField(_('Proof Reader'), default=False, help_text=_(
        'Designates whether this user should be treated as a Proof Reader. '
    ))
    is_printer = models.BooleanField(_('Printer'), default=False, help_text=_(
        'Designates whether this user should be treated as a Request Service. '
    ))
    USER_TYPE_CHOICES = (
        (1, 'أدمن'),
        (2, 'دار نشر'),
        (3, 'مترجم'),
        (4, 'مدقق لغوي'),
        (5, 'مصمم'),
        (6, 'كاتب'),
        (7, 'مطبعة'),
        (8, 'طالب خدمة'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, verbose_name=_('User Type'),
                                                 help_text=_(
                                                     'User Role in A system '
    ))

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'address']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return f"{self.first_name}"

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
