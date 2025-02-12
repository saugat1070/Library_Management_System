from django.contrib import admin
from api_LMS.models import UserRegistration
from api_LMS.models import Book_details
from api_LMS.models import IssueBook
from api_LMS.models import Book_Submission
# Register your models here.
admin.site.register(UserRegistration)
admin.site.register(Book_details)
admin.site.register(IssueBook)
admin.site.register(Book_Submission)