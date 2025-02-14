from django.db import models
from django.contrib.auth.hashers import make_password
from django.shortcuts import reverse

from courses.base_model import BaseModel


class User(BaseModel):
    ROL = [
        ('pr', 'Преподаватель'),
        ('st', 'Студент'),
        ('ad', 'Администратор'),
    ]
    STATUS = [
        ('ac', 'Активный'),
        ('in', 'Неактивный'),
    ]
    image = models.ImageField(upload_to='users_image/')
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=25, choices=ROL)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('users:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('users:delete', args=[self.pk])