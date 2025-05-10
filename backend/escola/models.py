from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User

# Create your models here.
class UserManager(BaseUserManager):
  def create_user(self, username, email, password, **extra_fields):
    if not username:
      raise ValueError('O campo username é obrigatório.')
    
    email = self.normalize_email(email)
    user = self.model(username=username, email=email, **extra_fields)

    user.set_password(password)
    user.save(using=self.db)
    return user
  
  def create_superuser(self, username, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if not extra_fields.get('is_staff'):
      raise ValueError('Superusuário precisa de is_staff=True')
    if not extra_fields.get('is_superuser'):
      raise ValueError('Superusuário precisa de is_superuser=True')
    
    return self.create_user(username, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
  OCUPPATION_CHOICES = [
    ('ADM', 'Administrador'),
    ('PRO', 'Professor'),
  ]

  name = models.CharField(max_length=200, blank=False) 
  phone = models.CharField(max_length=11, blank=False)
  occupation = models.CharField(max_length=3, choices=OCUPPATION_CHOICES, default='PRO', blank=False)

  objects = UserManager()

  def __str__(self):
    return self.username
  

class Classroom(models.Model):
  name = models.CharField(max_length=200, blank=False)
  professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)

class Meeting(models.Model):
  STATUS_CHOICES = [
    ('F', 'Finalizada'),
    ('A', 'Em andamento'),
    ('I', 'Inicia em breve'),
  ]

  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
  professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
  start_time = models.DateTimeField(blank=False)
  end_time = models.DateTimeField(blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=1, default='I', choices=STATUS_CHOICES ,blank=False)

