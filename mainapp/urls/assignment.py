from django.urls import path

from mainapp.views import assignment

patterns = [
    path('assignment/', assignment.assignment, name='assignment'),
]
