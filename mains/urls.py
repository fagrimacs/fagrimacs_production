from django.urls import path

from .import views

app_name = 'mains'

urlpatterns = [
    path('', views.Homepage.as_view(), name='name'),
]