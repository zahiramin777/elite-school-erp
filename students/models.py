from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

def student_photo_path(instance, filename):
    return f"students/{instance.admission_no}/photo_{timezone.now().strftime('%Y%m%d')}{filename.split('.')[-1]}"

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    admission_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    is_star_student = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=student_photo_path, null=True, blank=True)
    birth_certificate = models.FileField(upload_to='students/docs/', null=True, blank=True)

    def full_name(self): return f"{self.first_name} {self.last_name}"
    def __str__(self): return self.admission_no