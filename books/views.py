from django.shortcuts import render
from django.urls import reverse

from books.models import (
    Book,
    UserProfile,
PublisherNeeds
)

from books.forms import (
    BookForm,
    ProfileForm,
PublisherNeedsForm
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


class AddUserInfoView(CreateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'accounts/user-info.html'

    def form_valid(self, form):
        profile = form.save(commit=True)
        profile.user = self.request.user
        return super(AddUserInfoView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


class AddNeedsView(CreateView):
    model = PublisherNeeds
    form_class = PublisherNeedsForm
    template_name = 'books/add-needs.html'

    def form_valid(self, form):
        needs = form.save(commit=True)
        needs.publisher = self.request.user
        return super(AddNeedsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')
