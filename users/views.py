from django.shortcuts import render


def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def contact_view(request):
    return render(request, 'users/contact.html')

def policies_view(request):
    return render(request, 'users/policies.html')
