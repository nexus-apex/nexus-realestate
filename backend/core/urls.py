from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/create/', views.property_create, name='property_create'),
    path('properties/<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('properties/<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('inquiries/', views.inquiry_list, name='inquiry_list'),
    path('inquiries/create/', views.inquiry_create, name='inquiry_create'),
    path('inquiries/<int:pk>/edit/', views.inquiry_edit, name='inquiry_edit'),
    path('inquiries/<int:pk>/delete/', views.inquiry_delete, name='inquiry_delete'),
    path('showings/', views.showing_list, name='showing_list'),
    path('showings/create/', views.showing_create, name='showing_create'),
    path('showings/<int:pk>/edit/', views.showing_edit, name='showing_edit'),
    path('showings/<int:pk>/delete/', views.showing_delete, name='showing_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
