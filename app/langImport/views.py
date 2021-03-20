from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'langImport/home.html')

def import_page(request):
	return render(request, 'langImport/import.html')