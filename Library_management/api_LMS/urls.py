from django.urls import path
from api_LMS import views
# from rest_framework.authtoken.views import obtain_auth_token
from api_LMS.views import CustomJWTAuthToken
urlpatterns = [
    path('',views.home),
    path('register_page/',views.register.as_view(),name='register_page'),
    path('list_of_user/',views.list_of_user.as_view(),name='list_of_user'),
    path('user_profile/',views.UserProfile.as_view(),name='user_profile'),
    path('book_info/',views.Book_Details.as_view(),name='book_added'),
    path('book_info/<int:pk>',views.Update_Book.as_view(),name='update_book'),
    path('issue_book/',views.IssueBookView.as_view(),name='issue_book'),
    path('login/',CustomJWTAuthToken.as_view(),name='login'),

] 