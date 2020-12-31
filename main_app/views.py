from django.shortcuts import render

from django.http import HttpResponse

def home_page(request):
    return render(request, 'main_app/home.html')

def forum_page(request):
    return render(request, 'main_app/forum.html')

def lifeprep_page(request):
    return render(request, 'main_app/lifeprep.html')

def contact_page(request):
    return render(request, 'main_app/contact.html')

def partners_page(request):
    return render(request, 'main_app/partners.html')

def board_page(request):
    return render(request, 'main_app/board.html')

def financials_page(request):
    return render(request, 'main_app/financials.html')

def donate_page(request):
    return render(request, 'main_app/donate.html')

def dfactor_page(request):
    return render(request, 'main_app/board/davidfactor.html')