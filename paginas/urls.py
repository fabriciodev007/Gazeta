from django.urls import path
from .views import IdexView

urlpatterns = [
    path('', IdexView.as_view(), name='index'), 
]