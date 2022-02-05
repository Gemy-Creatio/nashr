from django.shortcuts import render
from main.models import (
    Homepage,
    WhoUS,
    About
)
# Create your views here.
from django.views import View


class HomepageView(View):
    def get(self, request):
        home_content = Homepage.get_solo()
        return render(request, 'main/homepage/homepage.html', {"content": home_content})


class WhoUsView(View):
    def get(self, request):
        who_content = WhoUS.get_solo()
        return render(request, 'main/whous/who-us.html', {"content": who_content})


class AboutView(View):
    def get(self, request):
        about_content = About.get_solo()
        return render(request, 'main/about/about-page.html', {"content": about_content})
