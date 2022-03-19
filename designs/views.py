from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView , View
from designs.models import (
    PrintBookRequest
)
from designs.forms import (
    PrintBookForm
)


class CreatePrintRequestView(CreateView):
    model = PrintBookRequest
    form_class = PrintBookForm
    template_name = 'books/print_books.html'

    def get_success_url(self):
        return reverse('dashboard')



class AllPrintRequestView(View):
    def get(self ,request):
        prints = PrintBookRequest.objects.all()
        return render(request , 'designs/all-prints.html' , context={"prints":prints})
        
