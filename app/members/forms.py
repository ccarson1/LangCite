from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
	native_lang = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'native_lang', 'password1', 'password1')


	def __init__(self, *args, **kwargs):
		super(UserRegForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['native_lang'].widget.attrs['class'] = 'form-control'
	