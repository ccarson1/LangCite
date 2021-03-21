from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
	return render(request, 'langImport/home.html')

def import_page(request):

	if request.method == "POST":
		up_method = request.POST['flexRadioDefault']
		if(up_method != 'Youtube url'):
			request.FILES['myfile']
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			yturl = 'no url';
		else:
			yturl = request.POST['yturl']
		
		
		up_title = request.POST['title']
		genre = request.POST['genre']
		up_public = request.POST['up_public']

		return render(request, 'langImport/import.html', {'yturl' : yturl})
	else:
		return render(request, 'langImport/import.html', {})

	