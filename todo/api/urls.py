from django.urls import include, path
from todo.api import views

urlpatterns = [
    path('', views.Home , name="api-2-home")
]
