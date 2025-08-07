from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class CustomUserCreationForm(UserCreationForm): #Custom user creation form 
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for all fields
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class TaskForm(forms.ModelForm): #Form for creating and updating tasks
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class TaskFilterForm(forms.Form): #Form for filtering tasks
    completed = forms.ChoiceField(
        choices=[('', 'All'), ('True', 'Completed'), ('False', 'Pending')],
        required=False,
        widget=forms.Select(attrs={'class': 'mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md'})
    )
    priority = forms.ChoiceField(
        choices=[('', 'All'), ('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')],
        required=False,
        widget=forms.Select(attrs={'class': 'mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md'})
    )