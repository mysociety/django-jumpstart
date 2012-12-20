from {{ project_name }}.shortcuts import render

def home(request):
    return render(request, 'index.html')

