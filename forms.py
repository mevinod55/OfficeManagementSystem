from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    taskname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Assigndate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    dateline =forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))

    class Meta:
        model = Task
        fields = ['name','taskname','Assigndate','dateline']
