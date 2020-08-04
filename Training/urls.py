"""Training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('traine/',views.traine,name="traine"),
    path('save_traine/', views.savetraine, name="save_traine"),
    path('td/',views.trainedashboard,name="traine_dashboard"),
    path('trainer/', views.trainer, name="trainer"),
    path('save_trainer/', views.savetrainer, name="save_trainer"),
    path('financial/', views.finacial, name="financial"),
    path('save_financial/', views.savefinacial, name="save_financial"),
    path('lead/',views.lead,name="lead"),
    path('prospect/', views.prospect, name="prospect"),
    path('Intraining/', views.Intraining, name="intraining"),
    path('completed/', views.completed, name="completed"),
    path('rejected/', views.rejected, name="rejected"),
    path('invalid/', views.invalid, name="invalid"),
    path('vtrainer/', views.vtrainer, name="vtrainer"),

]
