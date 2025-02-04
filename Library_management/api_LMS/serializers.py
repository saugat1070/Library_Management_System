from rest_framework import serializers
from api_LMS.models import UserRegistration

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = UserRegistration
        fields = ['email','first_name','last_name','photo_name','date_of_birth','college_name','password']
        extra_kwargs = {'oassword':{'write_only':True}}
    def create(self, validated_data):
        user = UserRegistration(**validated_data)
        user.set_password(validated_data["password"])  
        user.save()
        return user