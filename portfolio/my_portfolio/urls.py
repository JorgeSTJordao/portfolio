from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/', views.timeline, name='timeline'),
    path('description/<int:evento_id>/', views.descricao, name='descricao'),
]