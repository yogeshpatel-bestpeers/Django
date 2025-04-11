from django.db import models
from django.contrib.auth.models import User
# from account.models import User
from django.contrib.auth.hashers import make_password,check_password


class Student(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=70)
    password = models.CharField(max_length=255)




    
    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name




