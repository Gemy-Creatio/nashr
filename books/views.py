from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from books.models import (
    Book,
    UserProfile,
PublisherNeeds ,
BookDistrubuting ,
Negotiation
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

class AddBookDistrubView(View):
    def get(self,request):
        return render(request , 'books/add-bookDistub.html')


class BookChoicesView(View):
    def get(self,request):
        return render(request , 'books/bookchoices.html')


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

class NegtiationBookDistrubView(View):
    def get(self , request ,pk):
        book = BookDistrubuting.objects.get(pk=pk)
        return render(request , 'books/neg-book.html')
    def post(self , request , pk):
        book = BookDistrubuting.objects.get(pk=pk)
        period = request.POST.get('period')
        rights = request.POST.get('rights')
        ratio = request.POST.get('ratio')
        copies = request.POST.get('copies')
        price = request.POST.get('price')
        neg = Negotiation(book = book ,author_rights= rights ,author_ratio = ratio , number_of_copies = copies ,price = price )
        neg.save()
        return redirect('all-books')




class AllBookDistrubView(View):
    def get(self,request):
        context = {"books":BookDistrubuting.objects.exclude(user=request.user)}
        return render(request , 'books/alldistrub.html' , context=context)

