from django import forms
from .models import Lesson

class EditForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = ('lesson_title', 'genre_id', 'public', 'json_file')

		widgets = {
			'lesson_title' : forms.TextInput(attrs={'class': 'form-control'}),
			'genre_id' : forms.Select(attrs={'class': 'form-control'}),
			'json_file' : forms.Textarea(attrs={'class': 'form-control'})
		}