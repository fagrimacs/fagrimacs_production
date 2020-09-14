from django.urls import path

from .import views

app_name = 'admins'

urlpatterns = [
    path('dashboard/', views.AdminDashboard.as_view(), name='dashboard'),
    path('update-profile/<int:pk>/', views.AdminProfileView.as_view(), name='update-profile'),
    path('profile/<int:pk>/', views.AdminProfileDetailView.as_view(), name='profile'),
]