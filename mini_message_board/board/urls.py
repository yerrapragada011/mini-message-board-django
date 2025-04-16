from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_message, name='new_message'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
]
