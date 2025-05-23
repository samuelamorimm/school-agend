from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
# Create your views here.

class CustomAuthToken(ObtainAuthToken): #view customizada para login
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request': request})

    serializer.is_valid(raise_exception=True) #valida os campos do login ou retorna um erro
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)

    occupation = 'ADM'
    if user.occupation:
      occupation = user.occupation

    return Response({
      'token': token.key,
      'user_id': user.id,
      'username': user.username,
      'email': user.email,
      'occupation': occupation,
    })


class RegisterAdmView(APIView): #View para registro de ADM
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = RegisterAdmSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      
      return Response({
        "msg": "Adm cadastrado com sucesso!",
        "user": RegisterAdmSerializer(user).data
      }, status=status.HTTP_201_CREATED)
    
    return Response({
      "msg": "Erro ao criar adm."
    }, status=status.HTTP_400_BAD_REQUEST)

class RegisterProfessorView(APIView): #View para registro de professores
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = RegisterProfessorSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({
        "msg":"Professor cadastrado com sucesso!",
        "user": RegisterProfessorSerializer(user).data
      }, status=status.HTTP_201_CREATED)
    
    return Response({
      "msg": "Erro ao criar usuário",
    }, status=status.HTTP_400_BAD_REQUEST)
  
class MeetingViewSet(viewsets.ModelViewSet): #Crud nas agendas
  queryset = Meeting.objects.all()
  serializer_class = MeetingSerializer
  permission_classes = [IsAuthenticated]

class MeetingProfessorViewSet(viewsets.ModelViewSet): #Post de reunião passando automaticamente o professor
  queryset = Meeting.objects.all()
  serializer_class = MeetingSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(professor=self.request.user) #definindo o professor automaticamente se ele for o criador da mesma.

class ClassroomViewSet(viewsets.ModelViewSet): #CRUD de turmas
  queryset = Classroom.objects.all()
  serializer_class = ClassroomSerializer
  permission_classes = [IsAuthenticated]


class ListProfessorsViewSet(viewsets.ModelViewSet): #view para retornar todos os professores
  permission_classes = [IsAuthenticated]
  queryset = CustomUser.objects.all()
  serializer_class = RegisterProfessorSerializer

  def get_queryset(self):
    queryset = CustomUser.objects.filter(occupation='PRO')
    return queryset
  
class ListAdmsViewSet(viewsets.ModelViewSet): #view para retornar todos os adms
  permission_classes = [IsAuthenticated]
  queryset = CustomUser.objects.all()
  serializer_class = RegisterProfessorSerializer

  def get_queryset(self):
    queryset = CustomUser.objects.filter(occupation='ADM')
    return queryset


  

