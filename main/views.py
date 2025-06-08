# Importing packages.
# ------------------------------
import mpld3
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import JsonResponse
# ------------------------------

matplotlib.use('Agg')

# Loading data for LIFU study.
dfEFAT = pd.read_excel("/Users/armanmehzad/PycharmProjects/psychiatryScripts/lifuValuesArman136.xlsx", 0)  # Adjust path accordingly
subjects = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10']
cRawEFAT = ['con_0001', 'con_0002', 'con_0003', 'con_0004', 'con_0005', 'con_0006', 'con_0007', 'con_0008', 'con_0009',
            'con_0010', 'con_0011']
cEFAT = ['EFAT1', 'EFAT2', 'EFAT3', 'EFAT4', 'EFAT5', 'EFAT6', 'EFAT7', 'EFAT8', 'EFAT9', 'EFAT10', 'EFAT11']
dfEFAT['contrast'].replace(cRawEFAT, cEFAT, inplace=True)
ROIs = list(dfEFAT.columns)[4:]
dfEFAT_mean = dfEFAT.groupby(['pre / post', 'contrast'], as_index=False)[ROIs].mean()
dfEFAT_SE = dfEFAT.groupby(['pre / post', 'contrast'], as_index=False)[ROIs].sem()


def generate_multi_roi_graph(selected_rois):
    fig, ax = plt.subplots(figsize=(12, 8))

    for roi in selected_rois:
        # Get pre and post values for the ROI
        pre_means = dfEFAT_mean[dfEFAT_mean['pre / post'] == 'pre'][roi].values
        post_means = dfEFAT_mean[dfEFAT_mean['pre / post'] == 'post'][roi].values
        efat_labels = dfEFAT_mean['contrast'].unique()

        # Add to the graph
        ax.plot(efat_labels, pre_means, marker='o', label=f'{roi} (Pre)', linestyle='-')
        ax.plot(efat_labels, post_means, marker='x', label=f'{roi} (Post)', linestyle='--')

    ax.set_title('Pre/Post Comparison of Selected ROIs', fontsize=16)
    ax.set_xlabel('EFAT Contrasts', fontsize=14)
    ax.set_ylabel('Mean Intensity', fontsize=14)
    ax.legend(fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return mpld3.fig_to_html(fig)  # Converts the plot to HTML (interactive with mpld3)

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def research_page(request):
    # Get selected ROIs, defaults to all ROIs
    selected_rois = request.GET.getlist('roi', ROIs)

    # Generate graph for selected ROIs
    #plot_html = generate_multi_roi_graph(selected_rois)

    # Check if it's an AJAX request (used for updating dynamically)
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #    return JsonResponse({'updated_graph_html': plot_html})

    # Render the full template if not an AJAX request
    return render(request, 'main/research.html')
    #return render(request, 'main/research.html', {'plot_html': plot_html, 'rois': ROIs, 'selected_rois': selected_rois})
