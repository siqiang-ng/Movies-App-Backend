from django.forms import ModelForm
from .models import Movie
from django.forms.widgets import NumberInput

class MovieForm(ModelForm):
    class Meta: 
        model = Movie
        fields = "__all__"
        widgets = {
            'release_date': NumberInput(attrs={'type':'date'}),
        }
