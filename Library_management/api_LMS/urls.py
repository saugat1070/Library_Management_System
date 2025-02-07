from django.urls import path
from api_LMS import views

urlpatterns = [
    path('',views.home),
    path('register_page/',views.register.as_view(),name='register_page'),
    path('list_of_user/',views.list_of_user.as_view(),name='list_of_user'),
    path('user_profile/',views.UserProfile.as_view(),name='user_profile'),
    path('book_add/',views.Book_Details.as_view(),name='book_added'),
    path('issue_book/',views.IssueBook.as_view(),name='issue_book'),

] 