# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Lecturer(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Results(models.Model):
    stu = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    hallticket_no = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.CharField(max_length=30)

    def __str__(self):
        return self.marks
