from django.shortcuts import render, redirect

# Create your views here.
from .models import Contact



def home(request):
    return render(request, 'blog/blog.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(name = name, email = email, subject = subject, message = message)
        c.save()
        return redirect('contact')

    
    return render(request, 'pages/contact.html')

