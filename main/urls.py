from django.urls import path

from .import views

app_name = 'main'

urlpatterns = [
    path('', views.Homepage.as_view(), name='name'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
]
