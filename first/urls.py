"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import HomeView, department, user_signin, logout_view, sub_list, lec_list, res_list

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^department/', department, name='department'),
    url(r'^login/', user_signin, name='login'),
    url(r'^subjects', sub_list, name='subjects'),
    url(r'^lecturers', lec_list, name='lecturers'),
    url(r'^results', res_list, name='results'),
    url(r'^logout', logout_view, name='logout'),
    # url(r'^subject/<int:sub_user>', sub_by_user, name='sub_user')
]