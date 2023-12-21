from django.shortcuts import render


def home_page_view(request):
    return render(request, 'home_main.html')


def contact_page_view(request):
    return render(request, 'contact.html')
