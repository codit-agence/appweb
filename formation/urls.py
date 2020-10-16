from django.urls import path, include
from .views import formation_index


app_name = 'formation'

urlpatterns = [
    path('', formation_index, name='index'),

]
