from django.urls import path
from books.views import (
    AddBookView,
    AddNeedsView,
    AddBookDistrubView,
    BookChoicesView,
    NegtiationBookDistrubView,
    AllBookDistrubView,
    AllBookContracts,
    AllCopyrightsContracts,
    AddBookContract,
    AddCopyRightContract,
    ContractsChoices
)

urlpatterns = [
    path('add', AddBookView.as_view(), name='add-book'),
    path('add/needs', AddNeedsView.as_view(), name='add-needs'),
    path('add/rights', AddBookDistrubView.as_view(), name='add-rights'),
    path('choices', BookChoicesView.as_view(), name='book-choices'),
    path('negtiation/<int:pk>', NegtiationBookDistrubView.as_view(), name='neg-book'),
    path('all', AllBookDistrubView.as_view(), name='all-books'),
    path('copyright/add-contract',
         AddCopyRightContract.as_view(), name='add-copyright-contract'),
    path('contract/add', AddBookContract.as_view(),
         name='add-book-contract'),
    path('all/contracts', AllBookContracts.as_view(), name='all-books-contract'),
    path('all/copyrights/contract', AllCopyrightsContracts.as_view(),
         name='all-contracts-copyrights'),
    path('choices', ContractsChoices.as_view(), name='contract-choices'),

]
