from rest_framework import serializers
from .models import CustomUser, Meeting, Classroom

class RegisterProfessorSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = CustomUser
    fields = ['username', 'email','password', 'name', 'phone','occupation']

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      email=validated_data.get('email', ''), #opcional
      password=validated_data['password'],
      name=validated_data['name'],
      phone=validated_data['phone'],
      occupation='PRO',
    )
    return user
  
class RegisterAdmSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = CustomUser
    fields = ['username', 'email','password', 'name', 'phone','occupation']

  def create(self, validated_data):
    user = CustomUser.objects.create_superuser(
      username=validated_data['username'],
      email=validated_data.get('email', ''),
      password=validated_data['password'],
      name=validated_data['name'],
      phone=validated_data['phone'],
      occupation='ADM',
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



