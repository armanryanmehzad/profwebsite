# Importing packages.
# ------------------------------
from django.shortcuts import render
from django.http import JsonResponse

# ------------------------------

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def research_page(request):
    return render(request, 'main/research.html')
    #return render(request, 'main/research.html', {'plot_html': plot_html, 'rois': ROIs, 'selected_rois': selected_rois})

def publications_page(request):
    return render(request, 'main/publications.html')

def cv_page(request):
    return render(request, 'main/cv.html')

def contact_page(request):
    return render(request, 'main/contact.html')