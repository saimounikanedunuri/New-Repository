# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Results, Lecturer, Subject

# Register your models here.


class ResultsAdmin(admin.ModelAdmin):
        pass


class LecturerAdmin(admin.ModelAdmin):
        pass


class SubjectAdmin(admin.ModelAdmin):
        pass

admin.site.register(Results, ResultsAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Subject, SubjectAdmin)
