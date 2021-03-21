from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import LessonImportLib
# Create your views here.
def home(request):
	return render(request, 'langImport/home.html')

def import_page(request):

	if request.method == "POST":
		up_method = request.POST['flexRadioDefault']
		if up_method != 'Youtube url':
			request.FILES['myfile']
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			yturl = 'no url'
			if up_method == 'PDF':
				LessonImportLib.string_to_json(LessonImportLib.pdf_to_string('media/russian_folk.pdf', 'rus'))
		else:
			yturl = request.POST['yturl']
		
		
		up_title = request.POST['title']
		genre = request.POST['genre']
		up_public = request.POST['up_public']

		return render(request, 'langImport/import.html', {'up_method' : up_method})
	else:
		return render(request, 'langImport/import.html', {})

	