from django.urls import path
from .views import login_view, add_event_view

app_name = 'secret_add'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('add/', add_event_view, name='add'),
] 