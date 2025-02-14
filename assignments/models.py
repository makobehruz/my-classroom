from django.db import models
from django.shortcuts import reverse

from courses.base_model import BaseModel
from courses.models import Course


class Assignment(BaseModel):
    STATUS = [
        ('ac', 'Активный'),
        ('in', 'Неактивный'),
    ]
    job_title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    desc = models.TextField()
    end_date = models.DateField()
    max_score = models.PositiveIntegerField()
    status = models.CharField(max_length=25, choices=STATUS)

    def __str__(self):
        return self.job_title

    def get_update_url(self):
        return reverse('assignments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('assignments:delete', args=[self.pk])

