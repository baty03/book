from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:id>/', book_detail, name='book_detail'),
]