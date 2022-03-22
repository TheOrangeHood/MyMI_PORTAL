# from django.db import models

# Create your models here.
from django.db import models

class CoordieAssignedTask(models.Model):
    cg = models.TextField(max_length=30)
    coordieID = models.CharField(max_length=10)
    coordieEmail = models.EmailField(max_length=30)
    coordieTask = models.CharField(max_length=30)
    taskCompleted = models.BooleanField(default=False)