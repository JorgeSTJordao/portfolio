from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/', views.timeline, name='timeline'),
    path('descricao/<int:evento_id>/', views.descricao, name='descricao'),
    path('projetos/', views.projetos, name='projetos'),
]