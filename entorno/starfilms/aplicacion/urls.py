from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('',index ,name="index"),
    path('compraBoleto/' ,compraBoleto, name="compraBoleto"),
    path('sesion/', sesion, name="sesion"),
    path('jaws/', jaws, name="jaws"),
    path('thedriver/', thedriver, name="thedriver"),
    path('halloween/', halloween, name="halloween"),
    path('medioPago/', medioPago, name="medioPago"),
    path('agregar-persona/', agregar_persona, name='agregar_persona'),
    path('listar-personas/', listar_personas, name="listar_personas"),
    path('updatepersona/<id>',updatepersona,name="updatepersona"),
    path('eliminarPersona/<id>',eliminarpersona, name="eliminarpersona"),
    path('agregar_pelicula/', agregar_pelicula, name="agregar_pelicula"),
    path('listar_peliculas/', listar_peliculas, name="listar_peliculas"),
    path('eliminar_pelicula/<id>', eliminarpelicula, name="eliminarpelicula"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('administrador/', administrador, name='administrador'),
    path('login/app/administrador/', views.administrador, name='administrador'),

]