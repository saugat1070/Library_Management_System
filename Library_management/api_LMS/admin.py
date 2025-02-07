from django.contrib import admin
from api_LMS.models import UserRegistration
from api_LMS.models import Book_details
from api_LMS.models import IssueBook
# Register your models here.
admin.site.register(UserRegistration)
admin.site.register(Book_details)
admin.site.register(IssueBook)