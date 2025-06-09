# Importing packages.
# ------------------------------
from django.shortcuts import render
from django.http import JsonResponse
# ------------------------------

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def research_page(request):
    # Get selected ROIs, defaults to all ROIs
    # Generate graph for selected ROIs
    #plot_html = generate_multi_roi_graph(selected_rois)

    # Check if it's an AJAX request (used for updating dynamically)
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #    return JsonResponse({'updated_graph_html': plot_html})

    # Render the full template if not an AJAX request
    return render(request, 'main/research.html')
    #return render(request, 'main/research.html', {'plot_html': plot_html, 'rois': ROIs, 'selected_rois': selected_rois})
