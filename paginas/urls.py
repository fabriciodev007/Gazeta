from django.urls import path
from .views import IdexView, AssinarView, ContatView

urlpatterns = [
    path('', IdexView.as_view(), name='index'),
    path('/assinar',AssinarView.as_view(),name='assinar'), 
    path('/contato',ContatView.as_view(), name='contato')
]