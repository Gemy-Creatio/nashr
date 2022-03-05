from django.urls import reverse
from django.views.generic import CreateView
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
