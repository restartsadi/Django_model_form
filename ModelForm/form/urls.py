from django.urls import path

from . import views

urlpatterns = [
    path('contact/' , views.contact, name='contact'),
    path('create_student/' , views.create_student, name='create_student')
]
