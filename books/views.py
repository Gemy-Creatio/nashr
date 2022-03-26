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
    NegotiationBook,
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
from django.core.paginator import Paginator


class AddIntersetView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        user = request.user
        advertise = AdvertisePresent(publisher=user, book=book)
        advertise.save()
        return redirect('all-books')


class ApplyNeedsView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        user = request.user
        needs = NeedsPresent(user=user, needs=book)
        needs.save()
        return redirect('all-proof-requests')


class AllBookView(View):
    def get(self, request):
        books = Book.objects.exclude(user=request.user)
        paginator = Paginator(books, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'books/allbooks.html' , context={"books":page_obj})


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




class AddBookUserView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/addBooks.html'

    def get_success_url(self):
        return reverse('home-advertise', args=(self.object.pk,))


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
        rights = request.POST.get('rights')
        ratio = request.POST.get('ratio')
        copies = request.POST.get('copies')
        price = request.POST.get('price')
        neg = Negotiation(book=book, author_rights=rights,
                          author_ratio=ratio, number_of_copies=copies, price=price)
        neg.save()
        return redirect('all-books-distrub')

class NegtiationBookAdvertiseView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'books/neg-book.html')

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        rights = request.POST.get('rights')
        ratio = request.POST.get('ratio')
        copies = request.POST.get('copies')
        price = request.POST.get('price')
        neg = NegotiationBook(book=book, author_rights=rights,
                          author_ratio=ratio, number_of_copies=copies, price=price)
        neg.save()
        return redirect('all-books-contract')



class AllBookDistrubView(View):
    def get(self, request):
        books = BookDistrubuting.objects.exclude(user=request.user)
        paginator = Paginator(books, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"books": page_obj}
        return render(request, 'books/alldistrub.html', context=context)


class AllBookContracts(View):
    def get(self, request):
        contracts = BookContract.objects.filter(found=request.user)
        paginator = Paginator(contracts, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'books/all-books-contract.html', context={"contracts": page_obj})


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
        user_obj = User.objects.get(pk=user)
        book_obj = Book.objects.get(pk=book)
        file = request.FILES['contract']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        contract = BookContract(
            found=found, book=book_obj, author_name=user_obj, contract=file)
        contract.save()
        return redirect('all-books-contract')


class AddCopyRightContract(View):
    def get(self, request):
        books = Book.objects.filter(user=request.user)
        translators = User.objects.filter(user_type=2).exclude(pk = request.user.pk)
        context = {"books": books, "translators": translators}
        return render(request, 'books/addcopyrightscontract.html', context=context)

    def post(self, request):
        found = request.user
        book = request.POST.get('book')
        user = request.POST.get('user')
        user_obj = User.objects.get(pk=user)
        book_obj = Book.objects.get(pk=book)
        file = request.FILES['contract']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        contract = CopyRightContract(
            found=found, book=book_obj, author_name=user_obj, contract=file)
        contract.save()
        return reverse('all-contracts-copyrights')


class AllCopyrightsContracts(View):
    def get(self, request):
        contracts = CopyRightContract.objects.filter(found=request.user)
        paginator = Paginator(contracts, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"books": page_obj}
        return render(request, 'books/all-contract-copyrights.html', context={"contracts": contracts})


class ContractsChoices(View):
    def get(self, request):
        return render(request, 'books/contract-cohices.html')


class PublisherNeedsProofView(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='مدقق لغوى')
        paginator = Paginator(needs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'services/allneedsproof.html', context={"needs": page_obj})


class AllWriterNeeds(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='كاتب')
        paginator = Paginator(needs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'services/allneedsproof.html', context={"needs": page_obj})


class AllDesignerNeeds(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='مصمم')
        paginator = Paginator(needs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'services/allneedsproof.html', context={"needs": page_obj})


class AllTranslatorNeeds(View):
    def get(self, request):
        needs = PublisherNeeds.objects.filter(needs='مترجم')
        paginator = Paginator(needs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'services/allneedsproof.html', context={"needs": page_obj})




class AllBookCopyrightsNegView(View):
    def get(self ,request , pk):
        copyrights = BookDistrubuting.objects.get(pk=pk)
        negs = Negotiation.objects.filter(book=copyrights)
        paginator = Paginator(negs, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'books/allneg-copyrights.html', context={"negs":page_obj})


class AllBookAdvertisesNegView(View):
    def get(self ,request , pk):
        book = Book.objects.get(pk=pk)
        negs = NegotiationBook.objects.filter(book=book)
        paginator = Paginator(negs, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'books/allneg-advertise.html', context={"negs":page_obj})


class AllBookCopyrightsForPublisher(View):
    def get(self , request):
        copyrights = BookDistrubuting.objects.filter(user=request.user)
        paginator = Paginator(copyrights, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'books/allcopypublisher.html' , context={"books":page_obj})

class BooksForPublisherView(View):
    def get(self , request):
        return render(request , 'books/bookspublisher.html')
class AllBookAdvertiseForPublisher(View):
    def get(self , request):
        copyrights = Book.objects.filter(user=request.user)
        paginator = Paginator(copyrights, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'books/alladpublisher.html' , context={"books":page_obj})


class AcceptAdvertisetNeg(View):
    def get(self , request , pk):
        neg = NegotiationBook.objects.get(pk=pk)
        neg.is_accepted = True
        neg.save()
        return redirect('neg-all-advertise')



class AcceptCopyNeg(View):
    def get(self , request , pk):
        neg = Negotiation.objects.get(pk=pk)
        neg.is_accepted = True
        neg.save()
        return redirect('neg-all-copy')




class AllNegResultsAdvertise(View):
    def get(self , request):
        negs = NegotiationBook.objects.filter(user=request.user)
        paginator = Paginator(negs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'designs/allnegs-result.html' , context={"results":page_obj})



class AllNegResultsCopy(View):
    def get(self , request):
        negs = Negotiation.objects.filter(user=request.user)
        paginator = Paginator(negs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'designs/allnegs-result.html' , context={"results":page_obj})