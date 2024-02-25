from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save



# Create your models here.

class UserManager(BaseUserManager):
    def createuser(self, email, username,first_name,last_name, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username,first_name,last_name, password=None):
        user = self.createuser(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    RESTARUNT = 1
    CUSTOMER = 2
    ROLE_CHOICE = (
        (RESTARUNT, "Restarunt"),
        (CUSTOMER, "Customer"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=11, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pin_code = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def post_save_user_profile_receiver (sender, instance, created, **kwargs):
    print(created)
    if created:
        print('Profile Created')
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
        print('Updated')
@receiver(pre_save, sender=User)        
def pre_save_user_profile_receiver(sender, instance, *args, **kwargs):
    print(instance.username,'pre_save_user_profile_receiver')
    print(instance.email,'pre_save_user_profile_receiver')
    
    