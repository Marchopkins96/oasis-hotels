from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Hotel

class Home(generic.TemplateView):
    template_name = 'index.html'


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})

