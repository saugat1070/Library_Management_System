from rest_framework import serializers
from api_LMS.models import UserRegistration
from api_LMS.models import Book_details
from api_LMS.models import IssueBook
from api_LMS.models import Book_Submission

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = UserRegistration
        fields = ['email','first_name','last_name','photo_name','date_of_birth','college_name','password']
        extra_kwargs = {'password':{'write_only':True}}
    def create(self, validated_data):
        user = UserRegistration(**validated_data)
        user.set_password(validated_data["password"])  
        user.save()
        return user

    
class Book_detailsSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Book_details  
        fields = ['book_name', 'date_of_publication', 'book_photo', 'author_name','added_by']

class IssueBookSerializer(serializers.ModelSerializer):
    issue_by = serializers.StringRelatedField(read_only=True)
    author_of_book = serializers.StringRelatedField(read_only=True)
    college_name = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = IssueBook
        fields = '__all__'
class Book_SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Submission
        fields = ['issued_book','date_of_issue','date_of_submission','late_fee']
        extra_kwargs = {'issued_book':{'read_only':True},
                        'date_of_submission':{'read_only':True},
                        'date_of_issue':{'read_only':True},
                        'late_fee':{'read_only':True}}