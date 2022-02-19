from django.urls import path
from books.views import (
    AddBookView
)

urlpatterns = [
    path('add', AddBookView.as_view(), name='add-book')
]
