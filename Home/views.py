from django.shortcuts import render, HttpResponse
# message purpose import
from django.contrib import messages
from datetime import datetime

from Home.models import Contact
# Create your views here.
def index(request):
    context = {
        'name':'Omkar kurund'
    }
    return render(request,"index.html",context)
    # return HttpResponse('This is Home Page')

#about page
def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method== 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your Message has been sent!!...")
    return render(request,'contact.html')
