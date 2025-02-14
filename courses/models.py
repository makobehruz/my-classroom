from django.db import models
from django.shortcuts import reverse

from .base_model import BaseModel
from users.models import User


class Course(BaseModel):
    STATUS = [
        ('ac', 'Активный'),
        ('in', 'Неактивный'),
    ]
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    desc = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'rol': 'pr'}, related_name='courses', null=True)
    start_date = models.DateField()
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=25, choices=STATUS)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse('courses:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('courses:delete', args=[self.pk])