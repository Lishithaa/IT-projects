from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
]
