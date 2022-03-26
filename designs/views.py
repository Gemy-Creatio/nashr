from django.urls import reverse
from django.views.generic import CreateView , View
from designs.models import (
    PrintBookRequest , 
    BookFormating
)
from designs.forms import (
    PrintBookForm
)
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.core.paginator import Paginator




class CreatePrintRequestView(CreateView):
    model = PrintBookRequest
    form_class = PrintBookForm
    template_name = 'books/print_books.html'
    def form_valid(self, form):
        request = form.save(commit=True)
        if request.user.first_name:
            request.user = self.request.user
        request.save()
        return super(CreatePrintRequestView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')



class AllPrintRequestView(View):
    def get(self ,request):
        prints = PrintBookRequest.objects.exclude(user=request.user)
        paginator = Paginator(prints, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request , 'designs/all-prints.html' , context={"prints":page_obj})
        



class CreateFormationRequestView(View):
    def get(self , request):
        return render(request , 'designs/createformation.html')
    def post(self, request):
        book_size = request.POST.get('book_size')
        book_color = request.POST.get('book_color')
        font_type = request.POST.get('font_type')
        font_size = request.POST.get('font_size')
        drafts = request.POST.get('drafts')
        main_address = request.POST.get('main_address')
        main_font_type = request.POST.get('main_font_type')
        main_font_size = request.POST.get('main_font_size')
        main_font_color = request.POST.get('main_font_color')
        double_address = request.POST.get('double_address')
        sub_address = request.POST.get('sub_address')
        sub_font_type = request.POST.get('sub_font_type')
        sub_font_size = request.POST.get('sub_font_size')
        sub_font_color = request.POST.get('sub_font_color')
        ehda_page = request.POST.get('ehda_page')
        thank_page = request.POST.get('thank_page')
        book_intro = request.POST.get('book_intro')
        define_page = request.POST.get('define_page')
        intro_page = request.POST.get('ehda_page')
        notes = request.POST.get('notes')
        file = request.FILES['book_file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        format = BookFormating(book_size=book_size, book_color=book_color, font_type=font_type,
                                   font_size=font_size, drafts=drafts, main_address=main_address, main_font_type=main_font_type,
                                   main_font_size=main_font_size, main_font_color=main_font_color, double_address=double_address, sub_address=sub_address, sub_font_type=sub_font_type,
                                    sub_font_size=sub_font_size , sub_font_color=sub_font_color , ehda_page=ehda_page , thank_page=thank_page , book_intro=book_intro ,
                                     define_page=define_page , intro_page=intro_page , notes=notes , book_file=file)
        format.save()
        return redirect('register-service')
