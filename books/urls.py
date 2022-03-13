from django.urls import path
from books.views import (
    AddBookView,
    AddNeedsView,
    AddBookDistrubView,
    BookChoicesView,
    NegtiationBookDistrubView , 
    AllBookDistrubView
)

urlpatterns = [
    path('add', AddBookView.as_view(), name='add-book'),
    path('add/needs', AddNeedsView.as_view(), name='add-needs'),
    path('add/rights', AddBookDistrubView.as_view(), name='add-rights'),
    path('choices', BookChoicesView.as_view(), name='book-choices'),
    path('negtiation/<int:pk>', NegtiationBookDistrubView.as_view(), name='neg-book'),
    path('all', AllBookDistrubView.as_view(), name='all-books'),

]
