from django.urls import path

from .import views

app_name = 'equipments'

urlpatterns = [
    path('add-tractor/', views.AddTractorView.as_view(), name='add-tractor'),
    path('add-implement/', views.ImplementView.as_view(),
         name='add-implement'),
    path('tractors/', views.ListTractor.as_view(), name='tractors'),
    path('implements/', views.ListImplement.as_view(), name='implements'),
    path('tractor/<int:pk>/edit/', views.UpdateTractor.as_view(),
         name='update-tractor'),
    path('implement/<int:pk>/edit/', views.UpdateImplement.as_view(),
         name='update-implement'),
    path('tractor/<int:pk>/delete/', views.DeleteTractor.as_view(),
         name='delete-tractor'),
    path('implement/<int:pk>/delete/', views.DeleteImplement.as_view(),
         name='delete-implement'),
    path('subcategory/', views.implement_subcategory, name='subcategory'),
    path('all-tractors/', views.TractorListHome.as_view(),
         name='all-tractors'),
    path('all-implements/', views.ImplementListHome.as_view(),
         name='all-implements'),
    path('tractor/<int:pk>/detail/', views.TractorDetailView.as_view(),
         name='tractor-detail'),
    path('implement/<int:pk>/detail/', views.ImplementDetailView.as_view(),
         name='implement-detail'),
    path('tractor/category/<int:pk>/', views.TractorCategoryList.as_view(),
         name='tractor-category'),
    path('implement/category/<int:pk>/', views.ImplementCategoryList.as_view(),
         name='implement-category'),
]
