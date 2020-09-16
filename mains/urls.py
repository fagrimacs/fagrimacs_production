from django.urls import path

from .import views

app_name = 'mains'

urlpatterns = [
    path('', views.Homepage.as_view(), name='name'),
    path('about/', views.AboutView.as_view(), name='about'),
]
