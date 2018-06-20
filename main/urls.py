
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login',auth_views.LoginView.as_view(), name="login"),
    path('logout',auth_views.LogoutView.as_view(), name="logout"),
    path('register', views.RegistroUsuario.as_view(), name="register"),
    path('home', views.index, name= "home"),
    path('tareas', views.tareas, name= "tareas"),
    path('crear_tarea', views.crear_tarea, name= "crear_tarea"),
    path('eliminarTarea/<int:pk>', views.EliminarTarea.as_view(), name="eliminarTarea"),





]
