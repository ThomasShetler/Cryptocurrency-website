from django.forms import ModelForm
from .models import Info

#Create the form class.
class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = '__all__'