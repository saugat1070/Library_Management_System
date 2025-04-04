from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import random

class UserRegistrationManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        first_name = extra_fields.pop('first_name', 'Admin')
        last_name = extra_fields.pop('last_name', 'User')

        return self.create_user(email, first_name=first_name, last_name=last_name, password=password, **extra_fields)


class UserRegistration(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo_name = models.ImageField(upload_to='photos/', height_field=None, width_field=None, null=True, blank=True)
    username = models.CharField(max_length=8, unique=True, blank=True) 
    date_of_birth = models.DateField()
    college_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False) 
    objects = UserRegistrationManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth", "college_name"]  

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.get_username()
        super().save(*args, **kwargs)

    def get_username(self):
        
        username = f'{self.first_name[:4]}{random.randint(1,9)}'.lower()
        return username

    def has_perm(self, perm, obj=None):
        return self.is_superuser  # Superusers have all permissions

    def has_module_perms(self, app_label):
        return self.is_superuser  # Superusers have access to all modules
    
class Book_details(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=40)
    date_of_publication = models.DateField()
    date_of_added = models.DateField(auto_now=True)
    book_photo = models.ImageField(upload_to='book_details/', null=True )
    added_by = models.ForeignKey(UserRegistration,on_delete=models.CASCADE,related_name='user_name')

    def __str__(self):
        return self.book_name
    
class IssueBook(models.Model):
    issue_by = models.ForeignKey(UserRegistration,on_delete=models.CASCADE,null=False)
    Date_of_issue = models.DateTimeField(auto_now_add=True)
    name_of_book = models.ForeignKey(Book_details, on_delete=models.SET_NULL,null=True)
    author_of_book = models.CharField(max_length=100,null=True)
    college_name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.issue_by
    
class Book_Submission(models.Model):
    issued_book =models.ForeignKey(IssueBook,on_delete=models.SET_NULL,related_name='book_issue',null=True,blank=True)
    date_of_issue = models.DateField()
    date_of_submission = models.DateField()
    late_fee = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    submiited = models.BooleanField(default=False)

    def __str__(self):
        return self.issued_book
    
class StaffDetails(models.Model):
    staff_name = models.CharField(max_length=20)
    time_of_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_name
