from django.db import models

# Create your models here.

class Task(models.Model):
    taskName = models.CharField(max_length=300)
    taskDescription = models.TextField()
    taskTime = models.TimeField(auto_now=True)

    def __str__(self):
        return self.taskName
    
