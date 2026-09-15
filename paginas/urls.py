from django.urls import path
from .views import IdexView, AssinarView

urlpatterns = [
    path('', IdexView.as_view(), name='index'),
    path('/assinar',AssinarView.as_view(),name='assinar'), 
]