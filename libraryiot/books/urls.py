"""Books URLs."""

#Django
from django.urls import include, path

#Views
from books import views as books_views

urlpatterns = [
    path(route='api/v1/books', view=books_views.hello_world, name='books')
]