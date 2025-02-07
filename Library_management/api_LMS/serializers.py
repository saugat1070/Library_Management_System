from rest_framework import serializers
from api_LMS.models import UserRegistration
from api_LMS.models import Book_details

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
    author_name = serializers.CharField(source='UserRegistration.first_name',read_only = True)
    class Meta:
        model = Book_details.objects.all()
        fields = ['book_name','date_of_publication','book_photo']
