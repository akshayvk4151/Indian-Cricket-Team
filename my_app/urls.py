from django.urls import path
from . import views
app_name='my_app'

urlpatterns=[
    path('',views.my_app_index,name='home'),
    path('gallary',views.my_app_gallary,name='gallary'),
    path('players',views.my_app_players,name='players'),
    path('about',views.my_app_about,name='about'),
    path('contact',views.my_app_contact,name='contact'),

]