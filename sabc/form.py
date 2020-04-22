from django import forms

class TextData(forms.Form):
    text = forms.CharField(label="Paste Text Here",max_length=7000)
    