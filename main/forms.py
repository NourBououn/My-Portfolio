# forms.py
from django import forms

class CVUploadForm(forms.Form):
    cv = forms.FileField(label='Upload your CV')
