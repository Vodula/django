from django.urls import path
from .views import hello_world, about, guess_number

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('about/', about, name='about'),
    path('guess/', guess_number, name='guess_number'),
]
