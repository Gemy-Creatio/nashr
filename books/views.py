from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from accounts.models import User
from django.core.files.storage import FileSystemStorage

from books.models import (
    Book,
    NeedsPresent,
    UserProfile,
    PublisherNeeds,
    BookDistrubuting,
    Negotiation,
    BookContract,
    CopyRightContract,
    AdvertisePresent
)

from books.forms import (
    BookForm,
    ProfileForm,
    PublisherNeedsForm
)
# Create your views here.
from django.views.generic import CreateView


class AddIntersetView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        user = request.user
        advertise = AdvertisePresent(publisher=user, book=book)
        advertise.save()
        return reverse('all-books')


class ApplyNeedsView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        user = request.user
        needs = NeedsPresent(user=user, needs=book)
        needs.save()
        return reverse('all-proof-requests')


class AllBookView(View):
    def get(self, request):
        books = Book.objects.exclude(user=request.user)
        return render(request, 'books/allbooks.html')


class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/addBooks.html'

    def form_valid(self, form):
        book = form.save(commit=True)
        book.user = self.request.user
        return super(AddBookView, self).form_valid(form)

    def get_success_url(self):
        return reverse('complete-book', args=(self.object.pk,))


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
    def get(self, request):
        return render(request, 'books/add-bookDistub.html')

    def post(self, request):
        author_name = request.POST.get('author_name')
        address = request.POST.get('address')
        number_of_pages = request.POST.get('number_of_pages')
        year_of_release = request.POST.get('year_of_release')
        book_price = request.POST.get('book_price')
        time_finish = request.POST.get('time_finish')
        rights = request.POST.get('rights')
        author_ratio = request.POST.get('author_ratio')
        print_copies = request.POST.get('print_copies')
        time_own = request.POST.get('time_own')
        price = request.POST.get('price')
        language = request.POST.get('language')
        distrub = BookDistrubuting(user=self.request.user, auther_name=author_name, address=address, number_of_pages=number_of_pages, year=year_of_release,
                                   language=language, book_price=book_price, time_finish=time_finish,
                                   author_rights=rights, auther_profit=author_ratio, number_of_copies=print_copies, time_own=time_own, price=price)
        distrub.save()
        return redirect('dashboard')


class BookChoicesView(View):
    def get(self, request):
        return render(request, 'books/bookchoices.html')


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
    def get(self, request, pk):
        book = BookDistrubuting.objects.get(pk=pk)
        return render(request, 'books/neg-book.html')

    def post(self, request, pk):
        book = BookDistrubuting.objects.get(pk=pk)
        period = request.POST.get('period')
        rights = request.POST.get('rights')
        ratio = request.POST.get('ratio')
        copies = request.POST.get('copies')
        price = request.POST.get('price')
        neg = Negotiation(book=book, author_rights=rights,
                          author_ratio=ratio, number_of_copies=copies, price=price)
        neg.save()
        return redirect('all-books')


class AllBookDistrubView(View):
    def get(self, request):
        context = {"books": BookDistrubuting.objects.exclude(
            user=request.user)}
        return render(request, 'books/all-contract-copyrightsl', context=context)


class AllBookContracts(View):
    def get(self, request):
        contracts = BookContract.objects.filter(found=request.user)
        return render(request, 'books/all-books-contract.html', context={"contracts": contracts})


class AddBookContract(View):
    def get(self, request):
        books = Book.objects.filter(user=request.user)
        translators = User.objects.exclude(user_type__in=(1, 2, 7, 8))
        context = {"books": books, "translators": translators}
        return render(request, 'books/addcontract.html', context=context)

    def post(self, request):
        found = request.user
        book = request.POST.get('book')
        user = request.POST.get('user')
        file = request.FILES['contract']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        contract = BookContract(
            found=found, book__pk=book, user__pk=user, contract=file)
        contract.save()
        return reverse('all-books-contract')


class AddCopyRightContract(View):
    def get(self, request):
        books = Book.objects.filter(user=request.user)
        translators = User.objects.exclude(user_type__in=(1, 2, 7, 8))
        context = {"books": books, "translators": translators}
        return render(request, 'books/addcopyrightscontract.html', context=context)

    def post(self, request):
        found = request.user
        book = request.POST.get('book')
        user = request.POST.get('user')
        file = request.FILES['contract']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        contract = CopyRightContract(
            found=found, book__pk=book, user__pk=user, contract=file)
        contract.save()
        return reverse('all-contracts-copyrights')


class AllCopyrightsContracts(View):
    def get(self, request):
        contracts = CopyRightContract.objects.filter(found=request.user)
        return render(request, 'books/all-contract-copyrights.html', context={"contracts": contracts})


class ContractsChoices(View):
    def get(self, request):
        return render(request, 'books/contract-cohices.html')


class PublisherNeedsProofView(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='مدقق لغوى')
        return render(request, 'services/allneedsproof.html', context={"needs": needs})


class AllWriterNeeds(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='كاتب')
        return render(request, 'services/allneedsproof.html', context={"needs": needs})


class AllDesignerNeeds(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='مصمم')
        return render(request, 'services/allneedsproof.html', context={"needs": needs})


class AllTranslatorNeeds(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='مترجم')
        return render(request, 'services/allneedsproof.html', context={"needs": needs})