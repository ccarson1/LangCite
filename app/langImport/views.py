from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import LessonImportLib
import os
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Lesson
from .models import Genre
from .models import Language



# Create your views here.
class HomeView(ListView):
	model =Lesson
	template_name = 'langImport/home.html'


class LessonView(ListView):
	model = Lesson
	template_name = 'langImport/lessons.html'
class ReadView(DetailView):
	model = Lesson
	template_name = 'langImport/read.html'

def settings(request):
	return render(request, 'langImport/settings.html', {})

def import_page(request):

	
	if request.method == "POST":

		up_method = request.POST['flexRadioDefault']
		up_title = request.POST['title']
		genre = request.POST['genre']
		up_public = request.POST['up_public']
		userLang = request.POST['userLang']
		lessonLang = request.POST['lessonLang']
		authorName = request.POST['authorName']

		if lessonLang or userLang != "":
			
			if up_method != 'Youtube url':
				request.FILES['myfile']
				myfile = request.FILES['myfile']
				fs = FileSystemStorage()
				filename = fs.save(myfile.name, myfile)
				uploaded_file_url = fs.url(filename)
				yturl = 'no url'

				#saves json from pdf method
				if up_method == 'PDF':
					lesson_json = LessonImportLib.string_to_json(LessonImportLib.pdf_to_string('media/' + filename, 'rus'), lessonLang, 'English')
					newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), json_file = lesson_json)
					newlesson.save()
				#saves json from text file
				elif up_method == 'Text File':
					lesson_json = LessonImportLib.text_to_string('media/' + filename, lessonLang, 'English')
					newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), json_file = lesson_json)
					newlesson.save()
				#saves json from image
				elif up_method == 'Image':
					lesson_json = LessonImportLib.string_to_json(LessonImportLib.image_to_string('media/' + filename, 'rus'), lessonLang, 'English')
					newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), json_file = lesson_json )
					newlesson.save()
				#loads this page without youtube url selected
				return render(request, 'langImport/import.html', {'userLang' : userLang , 'authorName' : authorName, 'yturl' : yturl})
			else:
				#saves json from youtube url
				yturl = request.POST['yturl']
				lesson_json = LessonImportLib.youtube_to_json(LessonImportLib.extract_id(yturl), 'ru', 'en' )
				newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), json_file = lesson_json)
				newlesson.save()
				#loads this page when youtube url is selected
				return render(request, 'langImport/import.html', {'userLang' : userLang , 'authorName' : authorName, 'yturl' : yturl})
		else:
			lessonLang = "No Target Language!!!"
			return render(request, 'langImport/import.html', {'lessonLang' : lessonLang })
		

		
	else:
		return render(request, 'langImport/import.html', {})

	