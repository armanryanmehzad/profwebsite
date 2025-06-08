from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research_page, name='research_page')
]
