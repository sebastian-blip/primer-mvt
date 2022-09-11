from django import forms
from .models import Family


class PostForm(forms.ModelForm):
    nombre = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'nombre de la persona'}),
        required=True
    )
    parentesco = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Parentesco'}),
        required=True
    )
    edad = forms.IntegerField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Edad'}),
        required=True
    )
    fecha_nacimiento = forms.DateField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Fecha de nacimiento'}),
        required=True
    )

    class Meta:
        model = Family
        fields = ['nombre', 'parentesco', 'edad', 'fecha_nacimiento']
