from django.urls import path, include
from .views import gestion_index, gestion_service, gestion_blog, gestion_partner, gestion_contact, gestion_project,gestion_inscription



app_name = 'gestion'

urlpatterns = [
    path('', gestion_index, name='index'),
    path('service/', gestion_service, name='service'),
    path('blog/', gestion_blog, name='blog'),
    path('partner/', gestion_partner, name='partner'),

    path('contact/', gestion_contact, name='contact'),
    path('inscription/', gestion_inscription, name='inscription'),

    path('project/', gestion_project, name='project'),

]
