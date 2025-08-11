from django import forms
from .models import Plant, Content, Group

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'group', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da planta'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['plant', 'category', 'text', 'image']
        widgets = {
            'plant': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Texto do conteúdo'}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do grupo'}),
        }
