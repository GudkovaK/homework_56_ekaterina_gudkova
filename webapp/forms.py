from django import forms

class GuestEntryForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    
class SearchForm(forms.Form):
    name = forms.CharField(label = 'имя', required = False)