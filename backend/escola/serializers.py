from rest_framework import serializers
from .models import CustomUser, Meeting, Classroom

class ProfessorRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = CustomUser
    fields = ['username', 'email','password', 'name', 'phone','occupation']

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      email=validated_data.get('email', ''),
      password=validated_data['password'],
      name = validated_data['name'],
      phone = validated_data['phone'],
      ocupation = validated_data['ocuppation'],
    )
    return user
  
class AdmRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = CustomUser
    fields = ['username', 'email','password', 'name', 'phone','occupation']

  def create(self, validated_data):
    user = CustomUser.objects.create_superuser(
      username=validated_data['username'],
      email=validated_data.get('email', ''),
      password=validated_data['password'],
      name = validated_data['name'],
      phone = validated_data['phone'],
      ocupation = validated_data['ocuppation'],
    )
    return user
  
# registro de usuarios professor/adm acima =====================

class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Classroom
    fields = '__all__'



