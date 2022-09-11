from django.urls import path
from .views import ver_familia, post

app_name = 'mi_familia'
urlpatterns = [
    path('familia/', ver_familia, name='ver_familiar'),
    path('agregar/', post)
]