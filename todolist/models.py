from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.


@python_2_unicode_compatible
class Task(models.Model):
    taskText = models.CharField(max_length=300)
    startDate = models.DateTimeField()
    deadLineDate = models.DateTimeField()
    isDone = models.BooleanField(default=False)


    def __str__(self):
        return self.taskText

    def isOverdue(self):
        return self.deadLineDate < datetime.datetime.now()


