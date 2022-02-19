from django.shortcuts import render
from django.urls import reverse

from books.models import (
    Book,
)

from books.forms import (
    BookForm
)
# Create your views here.
from django.views.generic import CreateView


class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/addBooks.html'

    def form_valid(self, form):
        book = form.save(commit=True)
        book.user = self.request.user
        return super(AddBookView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home-page')
