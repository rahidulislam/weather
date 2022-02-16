from django import forms

class SearchForm(forms.Form):
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City Here'}))