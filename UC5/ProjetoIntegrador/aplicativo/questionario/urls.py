from django.urls import path
from . import views
urlpatterns = [
    path('questionario/', views.abrir_questionario, name='questionario'),
]
