from django.urls import path
from .views import *

urlpatterns = [
    path('hostelers/', hostelersList, name='hostelers'),
    path('hosteler/<str:pk>', hostelerDetails, name='hosteler-detail'),

    path('messbills/', messBill, name='mess-bill'),
    path('messbills/<str:pk>', messBillDetails, name='messbill-detail'),

    path('rooms/', roomsList, name='room-list'),
    path('rooms/<str:pk>', roomDetails, name='roomtype-detail'),
]