from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import LessonImportLib
import os
from django.core.files.storage import default_storage

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
				LessonImportLib.string_to_json(LessonImportLib.pdf_to_string('media/' + filename, 'rus'))
			elif up_method == 'Text File':
				LessonImportLib.text_to_string('media/' + filename)
			elif up_method == 'Image':
				LessonImportLib.string_to_json(LessonImportLib.image_to_string('media/' + filename, 'rus'))
		else:
			yturl = request.POST['yturl']
		
		
		up_title = request.POST['title']
		genre = request.POST['genre']
		up_public = request.POST['up_public']
		userLang = request.POST['userLang']
		lessonLang = request.POST['lessonLang']
		authorName = request.POST['authorName']

		return render(request, 'langImport/import.html', {'lessonLang' : lessonLang ,'userLang' : userLang , 'authorName' : authorName})
	else:
		return render(request, 'langImport/import.html', {})

	