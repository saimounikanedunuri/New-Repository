# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render


# Create your views here.
from django.views.generic.base import TemplateView
from .models import Subject, Results, Lecturer
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import LoginForm
from django.contrib.auth import logout


class HomeView(TemplateView):
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html')


def department(request):
    return render(request, 'department.html')


def student_list(request):
    students = Student.objects.all()
    context = 'students : students'
    return render(request, 'student_list.html', context)


def user_signin(request):
    subs = []
    lecs = []
    results = []
    form = None
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            userObj = form.cleaned_data
            username = str(userObj['username'])
            password = str(userObj['password'])

            user = authenticate(username=username, password=password)

            if user is not None:
                print("rech")
                login(request, user)
                print(user)

            else:
                print("User error")
    elif request.user.is_authenticated() and request.method == 'GET':
        print("first")
        results.append(Results.objects.filter(stu=request.user))
        # for r in results:
        #     sub = Subject.objects.get(pk=r.subject.pk)
        #     subs.append(sub)
        #
        # for s in subs:
        #     lec = Lecturer.objects.get(pk=s.lecturer.pk)
        #     lecs.append(lec)
    else:
        form = LoginForm()

    print("n")
    #print(results[0])
    return render(request, 'login.html', {'form': form, 'results': results})


#def stu_by_id(request, stu_id):
 #   stu = User.objects.get(pk=stu_id)
  #  context = {'stu': stu}
   # return render(request, 'login.html', context)


#def lec_list(request):
    #lecturers = Lecturer.objects.all()
    #context = {'lecturers': lecturers}
    #return render(request, 'lec_list.html', context)


def res_list(request):
    results = Results.objects.filter(stu_id=request.user)
   # print (results[0])
    context = {'results': results}
    return render(request, 'res_list.html', context)


def sub_list(request):
    results = Results.objects.filter(stu=request.user)
    print (results[0])
    subs = []
    for r in results:
        sub = Subject.objects.get(pk=r.subject.pk)
        subs.append(sub)

    context = {'results': results, 'subjects': subs}
    return render(request, 'sub_list.html', context)


def lec_list(request):
    results = Results.objects.filter(stu=request.user)
    subs = []
    for r in results:
        sub = Subject.objects.get(pk=r.subject.pk)
        subs.append(sub)

    lecs = []
    for s in subs:
        lec = Lecturer.objects.get(pk=s.lecturer.pk)
        lecs.append(lec)
    context = {'results': results, 'subjects': subs, 'lecturers': lecs}
    return render(request, 'lec_list.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

#
# def sub_by_user(request, sub_user):
#     subject = (pk.=sub_user)
#     context = {'subject': subject}
#     return render(request, 'sub_detail.html', context)

