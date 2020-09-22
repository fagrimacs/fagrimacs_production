from django.urls import path

from .import views

app_name = 'equipments'

urlpatterns = [
    path('tractors/', views.TractorListView.as_view(),
         name='tractors-list'),
    path('add-tractor/', views.TractorAddView.as_view(), name='tractor-add'),
    path('tractor/<int:pk>/', views.TractorDetailView.as_view(),
         name='tractor-detail'),
    path('tractor/<int:pk>/update/', views.TractorUpdateView.as_view(),
         name='tractor-update'),
    path('tractor/<int:pk>/delete/', views.TractorDeleteView.as_view(),
         name='tractor-delete'),
    path('implements/', views.ImplementListView.as_view(),
         name='implements-list'),
    path('add-implement/', views.ImplementAddView.as_view(),
         name='implement-add'),
    path('implement/<int:pk>/detail/', views.ImplementDetailView.as_view(),
         name='implement-detail'),
    path('implement/<int:pk>/update/', views.ImplementUpdateView.as_view(),
         name='implement-update'),
    path('implement/<int:pk>/delete/', views.ImplementDeleteView.as_view(),
         name='implement-delete'),
    path('subcategory/', views.implement_subcategory, name='subcategory'),
    path('tractor/category/<int:pk>/', views.TractorCategoryList.as_view(),
         name='tractor-category'),
    path('implement/category/<int:pk>/', views.ImplementCategoryList.as_view(),
         name='implement-category'),
]
