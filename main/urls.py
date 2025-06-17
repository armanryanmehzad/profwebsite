from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research_page, name='research_page'),
    path('publications/', views.publications_page, name='publications_page'),
    path('cv/', views.cv_page, name='cv_page'),
    path('contact/', views.contact_page, name='contact_page')
]
