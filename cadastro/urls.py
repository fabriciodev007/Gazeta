from django.urls import path
from .views import UserViews

urlpatterns = [
    path('cadastro/', UserViews.as_view(), name='cadastro'),
]