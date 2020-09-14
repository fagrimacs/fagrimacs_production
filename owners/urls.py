from django.urls import path

from .import views

app_name = 'owners'

urlpatterns = [
    path('dashboard/', views.OwnerDashboard.as_view(), name='dashboard'),
    path('update-profile/<int:pk>/', views.OwnerProfileView.as_view(), name='update-profile'),
    path('profile/<int:pk>/', views.OwnerProfileDetailView.as_view(), name='profile'),
]