from django.urls import path
from books.views import (
    AddBookView,
    AddNeedsView
)

urlpatterns = [
    path('add', AddBookView.as_view(), name='add-book'),
    path('add/needs', AddNeedsView.as_view(), name='add-needs')

]
