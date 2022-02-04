from django.shortcuts import render
from main.models import (
    Homepage
)
# Create your views here.
from django.views import View


class HomepageView(View):
    def get(self, request):
        home_content = Homepage.get_solo()
        return render(request, 'main/homepage/homepage.html', {"content": home_content})
