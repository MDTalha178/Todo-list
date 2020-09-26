from django import forms
from athar_app.models import Loosers

class TaskForm(forms.ModelForm):
    class Meta:
        model = Loosers
        fields = ['loosers', 'done']