from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section', views.section, name='section'),
    path('section_post', views.section_post, name='section_post')
]
