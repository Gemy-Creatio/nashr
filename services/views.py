from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView
from nashr.settings import PROFILE_KEY, PAYTAB_API_SERVERKEY, API_ENDPOINT
import json
import requests
from django.contrib import messages


from books.models import (
    Book,
    BookContract ,
    CopyRightContract
)

from services.models import (
    TranslateService,
    RequestDesignService,
    Vouchers,
    PaidVoucher,
    TranslationRequest,
    SubtitleService,
    PersonWork , 
    ContactRequestServices
)
from services.forms import (
    TrnaslateServiceForm,
    SubttileServiceForm
)
from designs.forms import (
    TakeDesignForm
)
from designs.models import (
    TakeDesign
)


def AllVouchers(request):
    vouchers = Vouchers.objects.filter(user=request.user.pk, is_paid=False)
    paginator = Paginator(vouchers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services/all_vouchers.html', context={"vouchers": page_obj})


def AllWorks(request):
    works = PersonWork.objects.filter(user=request.user.pk)
    paginator = Paginator(works, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services/all_works.html', context={"works": page_obj})

class AllMessagesView(View):
    def get(self, request):
        msgs = ContactRequestServices.objects.filter(user=request.user)
        paginator = Paginator(msgs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "services/all-msgs.html", context={"msgs": page_obj})


def PayVoucher(request, pk):
    try:
        voucher = Vouchers.objects.get(pk=pk)
        paid = PaidVoucher(voucher=voucher)
        paid.save()
        payload = {
            "profile_id": PROFILE_KEY,
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_description": f"{voucher.description}",
            "cart_id": "50",
            "cart_currency": "sar",
            "cart_amount": int(voucher.amount),
            "callback": "https://naashr.co",
            "return": "https://naashr.co/"
        }
        headers = {
            "authorization": PAYTAB_API_SERVERKEY,
            "Content-Type": 'application/json; charset=utf-8'
        }
        r = requests.post(API_ENDPOINT, data=json.dumps(
            payload), headers=headers)
        data = json.dumps(r.json())
        content = json.loads(data)
        voucher.is_paid = True
        voucher.save()
        return redirect(content['redirect_url'])
    except:
        messages.error(request,
                       "حدث خطأ ")
        return redirect('all-vouchers')


class TranslationRequestView(View):
    def get(self, request, pk):
        return render(request, 'dashboard/addbooktranlation.html')

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        translator_intro = request.POST.get('translator_intro')
        dedication_page = request.POST.get('dedication_page')
        thank_page = request.POST.get('thank_page')
        define_page = request.POST.get('define_page')
        intro_page = request.POST.get('intro_page')
        content_page = request.POST.get('content_page')
        source_page = request.POST.get('source_page')
        draw_page = request.POST.get('draw_page')
        table_page = request.POST.get('table_page')
        cmyk_page = request.POST.get('cmyk_page')
        note = request.POST.get('note')
        file = request.FILES['contract']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        trans = TranslationRequest(book=book, translator_introduction=translator_intro, dedication_page=dedication_page,
                                   thank_you_page=thank_page, intro_page=intro_page, content_pages=content_page, source_page=source_page,
                                   supplements_page=define_page, page_images=draw_page, draws_page=table_page, CMYK_page=cmyk_page, note=note, contact=file)
        trans.save()
        return redirect('dashboard')


class RequestTranslateServiceView(CreateView):
    model = TranslateService
    form_class = TrnaslateServiceForm
    template_name = 'services/design_service.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_anonymous == False:
            self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_anonymous:
            return reverse('register-service')
        else:
            return reverse('dashboard')


class RequestSubtitleServiceView(CreateView):
    model = SubtitleService
    form_class = SubttileServiceForm
    template_name = 'designs/subtitle_service.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_anonymous == False:
            self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user != None:
            return reverse('dashboard')
        else:
            return reverse('register-service')

class AllBooksForTranslatorView(View):
    def get(slef ,request):
        books = Book.objects.exclude(user = request.user)
        paginator = Paginator(books, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'books/allbooks.html' , context={"books":page_obj})



class RequestDesignServiceView(View):
    def get(self, request):
        return render(request, 'services/translate_service.html')

    def post(self, request):
        book_size = request.POST.get('book_sizes')
        book_title = request.POST.get('book_title')
        author_name = request.POST.get('author_name')
        translator_name = request.POST.get('translator_name')
        scientific_rank = request.POST.get('scientific_rank')
        version_number = request.POST.get('version_number')
        house_logo = request.POST.get('house_logo')
        author_name_tail = request.POST.get('author_name_tail')
        translator_name_tail = request.POST.get('translator_name_tail')
        scientific_rank_tail = request.POST.get('scientific_rank_tail')
        part_number = request.POST.get('part_number')
        version_number_tail = request.POST.get('version_number_tail')
        about_book = request.POST.get('about_book')
        isbn = request.POST.get('isbn')
        house_information = request.POST.get('house_information')
        email = request.POST.get('email')
        notes = request.POST.get('notes')

        file = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        design_request = RequestDesignService(book_size=book_size, title_book=book_title, author_name=author_name,
                                              translator_name=translator_name, scientific_rank=scientific_rank,
                                              version_number=version_number, house_logo=house_logo,
                                              author_name_tail=author_name_tail,
                                              translator_name_tail=translator_name_tail,
                                              scientific_rank_tail=scientific_rank_tail, part_number=part_number,
                                              version_number_tail=version_number_tail, about_book=about_book,
                                              isbn_number=isbn, images=file,
                                              house_info=house_information, communication=email, note=notes
                                              )
        design_request.save()
        if self.request.user.is_anonymous == False:
            design_request.user = self.request.user
        design_request.save()
        return redirect('register-service')


class AllServicesForDesignView(View):
    def get(self, request):
        requests = RequestDesignService.objects.filter(is_shown_designer=True)
        paginator = Paginator(requests, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'dashboard/all_designs.html', context={"designs": page_obj})


class RequestServiceDetails(DetailView):
    model = RequestDesignService
    template_name = 'designs/design_detail.html'


class CreateTakeDesignRequest(CreateView):
    model = TakeDesign
    form_class = TakeDesignForm
    template_name = 'designs/TakeDesign.html'

    def form_valid(self, form):
        take_Design = form.save(commit=True)
        take_Design.user = self.request.user
        take_Design.save
        return super(CreateTakeDesignRequest, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


class HomeTranslationRequestView(View):
    def get(self, request):
        return render(request, 'services/add-bookadvertise.html')

    def post(self, request):
        translator_intro = request.POST.get('translator_intro')
        dedication_page = request.POST.get('dedication_page')
        thank_page = request.POST.get('thank_page')
        define_page = request.POST.get('define_page')
        intro_page = request.POST.get('intro_page')
        content_page = request.POST.get('content_page')
        source_page = request.POST.get('source_page')
        draw_page = request.POST.get('draw_page')
        table_page = request.POST.get('table_page')
        cmyk_page = request.POST.get('cmyk_page')
        note = request.POST.get('note')
        file = request.FILES['contract']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        trans = TranslationRequest(translator_introduction=translator_intro, dedication_page=dedication_page,
                                   thank_you_page=thank_page, intro_page=intro_page, content_pages=content_page, source_page=source_page,
                                   supplements_page=define_page, page_images=draw_page, table_page=table_page, CMYK_page=cmyk_page, note=note, contact=file)
        trans.save()
        return redirect('register-service')



class PersonalContractChoices(View):
    def get(self , request):
        return render(request , 'services/personal-choices.html')


class AllCopyContractsForUser(View):
    def get(self , request):
        contracts = CopyRightContract.objects.filter(author_name = request.user)
        paginator = Paginator(contracts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'services/copycontract-person.html' , context={"contracts":page_obj})


class AllBookContractsForUser(View):
    def get(self , request):
        contracts = BookContract.objects.filter(author_name = request.user)
        paginator = Paginator(contracts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'services/bookcontract-person.html' , context={"contracts":page_obj})



class AcceptCopyrightContract(View):
    def get(self , request , pk):
        contract = CopyRightContract.objects.get(pk=pk)
        contract.is_accepted = True
        contract.save()
        return redirect('all-copycontract-user')

class AcceptBookContract(View):
    def get(self , request , pk):
        contract = BookContract.objects.get(pk=pk)
        contract.is_accepted = True
        contract.save()
        return redirect('all-bookcontract-user')