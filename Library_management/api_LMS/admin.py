from django.contrib import admin
from api_LMS.models import UserRegistration
from api_LMS.models import Book_details
from api_LMS.models import IssueBook
from api_LMS.models import Book_Submission
# Register your models here.
#admin.site.register(UserRegistration)
@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['username','password']
admin.site.register(Book_details)
admin.site.register(IssueBook)
# admin.site.register(Book_Submission)
@admin.register(Book_Submission)
class Book_SubmissionAdmin(admin.ModelAdmin):
    list_display = ['issued_book','date_of_issue','date_of_submission','late_fee','submiited']