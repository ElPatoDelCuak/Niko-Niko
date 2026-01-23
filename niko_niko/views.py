from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'niko_niko/home.html')

def recipe(request):
    return render(request, 'niko_niko/recipe.html')

def about(request):
    return render(request, 'niko_niko/about.html')

def contact(request):
    return render(request, 'niko_niko/contact.html')