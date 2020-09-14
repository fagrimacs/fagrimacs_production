from django.urls import path

from .import views

app_name = 'experts'

urlpatterns = [
    path('dashboard/', views.ExpertDashboard.as_view(), name='dashboard'),
    path('update-profile/<int:pk>/', views.ExpertProfileView.as_view(), name='update-profile'),
    path('profile/<int:pk>/', views.ExpertProfileDetailView.as_view(), name='profile'),
]