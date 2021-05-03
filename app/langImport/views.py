from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import LessonImportLib as IM
import os
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Lesson
from .models import Genre
from .models import Language
from .forms import EditForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import JsonResponse



# Create your views here.
class HomeView(ListView):
	model =Lesson
	template_name = 'langImport/home.html'
	ordering = ['-id'] # changes the order of the lessons displayed

class LessonView(ListView):
	model = Lesson
	template_name = 'langImport/lessons.html'

class ReadView(DetailView):
	model = Lesson
	template_name = 'langImport/read.html'

	def post(self, request, pk):
		btn_word = request.POST.get('btn_word')
		btn_target = request.POST.get('btn_target')
		btn_native = request.POST.get('btn_native')
		print(btn_word)
		print(type(btn_target))
		print(btn_native)
		print(pk)
		if request.is_ajax():
			native_word = btn_word + "/" + btn_target + "/" + btn_native;
			# native_word = IM.translate_string(btn_word, 'en', 'fr')
			return JsonResponse({'native_word' : native_word}, status=200)
		return render(request, 'langImport/read.html' )
	


def settings(request):
	return render(request, 'langImport/settings.html', {})

def import_page(request):

	
	if request.method == "POST":

		#posts the data from the import form and sets them to variables
		up_method = request.POST['flexRadioDefault']
		up_title = request.POST['title']
		genre = request.POST['genre']
		up_public = request.POST['public']
		userLang = request.POST['userLang']
		lessonLang = request.POST['lessonLang']
		authorName = request.POST['authorName']



		if userLang or lessonLang != "":
			#gets the file from the file uploader if the youtube url option is not selected
			if up_method != 'Youtube url':
				request.FILES['myfile']
				myfile = request.FILES['myfile']
				fs = FileSystemStorage()
				filename = fs.save(myfile.name, myfile)
				uploaded_file_url = fs.url(filename)
				yturl = 'no url'

				#sets the language references for supported languages
				if userLang == "English":
					native_lang = 'en'
				if userLang == "Russian":
					native_lang = 'rus'
				if userLang == "Spanish":
					native_lang = 'spa'
				if userLang == "French":
					native_lang = 'fra'
				if lessonLang == "Russian":
					translate_lang = 'rus'
				if lessonLang == "French":
					translate_lang = 'fra'
				if lessonLang == "Spanish":
					translate_lang = 'spa'
				if lessonLang == "English":
					translate_lang = 'en'

				#saves json from pdf method
				if up_method == 'PDF':
					lesson_json = IM.string_to_json(str(IM.remove_control_characters(IM.string_to_json_format(IM.pdf_to_string('media/' + filename, translate_lang), lessonLang, userLang, up_method, up_title))))
					newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), public = up_public, json_file = lesson_json)
					newlesson.save()
				#saves json from text file
				elif up_method == 'Text File':
					lesson_json = IM.text_to_string('media/' + filename, lessonLang, userLang, up_method, up_title)
					newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), public = up_public, json_file = lesson_json)
					newlesson.save()
				#saves json from image
				elif up_method == 'Image':
					lesson_json = IM.string_to_json(str(IM.remove_control_characters(IM.string_to_json_format(IM.image_to_string('media/' + filename, translate_lang), lessonLang, userLang, up_method, up_title))))
					newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), public = up_public, json_file = lesson_json )
					newlesson.save()
				#loads this page without youtube url selected
				return render(request, 'langImport/import.html', {'up_public' : up_public , 'up_public' : up_public, 'yturl' : yturl})
			else:
				#sets the language references for supported languages for YouTube URLs
				if userLang == "English":
					native_lang = 'en'
				if userLang == "Russian":
					native_lang = 'ru'
				if userLang == "Spanish":
					native_lang = 'es'
				if userLang == "French":
					native_lang = 'fr'
				if lessonLang == "Russian":
					translate_lang = 'ru'
				if lessonLang == "English":
					translate_lang = 'en'
				if lessonLang == 'Spanish':
					translate_lang = 'es'
				if lessonLang == "French":
					translate_lang = 'fr'

				#saves json from youtube url
				yturl = request.POST['yturl']
				lesson_json = IM.youtube_to_json(IM.extract_id(yturl), translate_lang, native_lang, up_title )
				newlesson = Lesson.objects.create(lesson_title = up_title, user_id = request.user, language_id = Language.objects.get(language_name = lessonLang), genre_id = Genre.objects.get(genre_name = genre), public = up_public, json_file = lesson_json)
				newlesson.save()
				#loads this page when youtube url is selected
				return render(request, 'langImport/import.html', {'userLang' : userLang , 'authorName' : authorName, 'yturl' : yturl})
		else:
			if lessonLang == "":
				lessonLang = "No Target Language!!!"
			if userLang == "":
				userLang = "No Native language selected!!!"
			return render(request, 'langImport/import.html', {'lessonLang' : lessonLang, 'userLang' : userLang })
		

		
	else:
		return render(request, 'langImport/import.html', {})


class EditLessonView(UpdateView):
	model = Lesson
	form_class = EditForm
	template_name = 'langImport/edit_lesson.html'
	# fields = ['lesson_title', 'genre_id', 'public', 'json_file' ]

class DeleteLessonView(DeleteView):
	model = Lesson
	template_name = 'langImport/delete_lesson.html'
	success_url = reverse_lazy('web-lessons')