from django.urls import path
from . import views
from .views import contactt_list, contactt_detail, contactt_create, contactt_edit, contactt_delete

urlpatterns = [
    path('', views.contactt_list, name='contactt_list'),
    path('contacts/<int:pk>/', contactt_detail, name='contactt_detail'),
    path('contacts/new/',views.contactt_create, name='contactt_create'),
    path('contacts/<int:pk>/edit/', contactt_edit, name='contactt_edit'),
    path('contacts/<int:pk>/delete/', contactt_delete, name='contactt_delete'),
]




