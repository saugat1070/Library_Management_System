from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from api_LMS.models import UserRegistration
from api_LMS.models import Book_details
from api_LMS.serializers import UserRegistrationSerializer
from api_LMS.serializers import Book_detailsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from api_LMS.models import IssueBook
from api_LMS.serializers import IssueBookSerializer
from api_LMS.models import Book_Submission
from api_LMS.serializers import Book_SubmissionSerializer
from rest_framework import status
from api_LMS.serializers import Book_SubmissionSerializer
# Create your views here.

def home(self):
    return HttpResponse("<h1>RestFul API</h1>")

class register(generics.CreateAPIView):
    queryset = UserRegistration
    serializer_class = UserRegistrationSerializer

class list_of_user(generics.ListAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegistrationSerializer

    def get_object(self):
        return self.request.user

        
class Book_Details(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book_details.objects.all()
    serializer_class = Book_detailsSerializer

    def perform_create(self, serializer):
        return serializer.save(added_by = self.request.user)
# --> using APIview method
# class Update_Book(APIView):
#     permission_classes = [IsAuthenticated]
#     def get_object(self,pk):
#         try:
#             return Book_details.objects.get(pk = pk)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#     def get(self,request,pk,format=None):
#         book = self.get_object(pk)
#         serializer = Book_detailsSerializer(book)
#         return Response(serializer.data)
    
#     def put(self,request,pk,format=None):
#         book = self.get_object(pk)
#         serializer = Book_detailsSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Update_Book(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book_details.objects.all()
    serializer_class = Book_detailsSerializer
    lookup_field = 'pk'
# class IssueBookView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self,request,format=None):
#         issuebook = IssueBook.objects.all()
#         serializer = IssueBookSerializer(issuebook, many = True)
#         return Response(serializer.data)

#     def post(self,request,format=None):
#         serializer = IssueBookSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save(issue_by=request.user,
#                             author_of_book=request.data.get('name_of_author'),
#                             college_name=request.user.college_name)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class IssueBookView(generics.ListCreateAPIView):
    queryset = IssueBook.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = IssueBookSerializer

    def perform_create(self, serializer):
        book_id = self.request.data.get('name_of_book')
        author_of_book = None
        try:
            book = Book_details.objects.get(id = int(book_id))
            if book:
                author_name = book.author_name
            else:
                print('book is not found')
        except:
            author_name = 'Unknown'
        serializer.save(issue_by=self.request.user,
                               author_of_book=author_name,
                               college_name=self.request.user.college_name)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


class BookSubmission(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,format=None):
        data = Book_Submission.objects.all()
        serializer = Book_SubmissionSerializer(data, many = True)
    
    def post(self,request,format=None):
        pass



    
