from django.urls import path

from .import views

app_name = 'farmers'

urlpatterns = [
    path('dashboard/', views.FarmerDashboard.as_view(), name='dashboard'),
    path('update-profile/<int:pk>/', views.FarmerProfileView.as_view(), name='update-profile'),
    path('profile/<int:pk>/', views.FarmerProfileDetailView.as_view(), name='profile'),
]