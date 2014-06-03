from django import forms
from discoveries.models import PartDiscovered
         
class SaForm(forms.Form):
    LIST_INTERESTS = PartDiscovered.objects.all()

    LIST_INTERESTS = (
        ('Energy', 'Energy'),
        ('Business', 'Business'),
        ('Social', 'Social'),
        ('Mobile', 'Mobile'),
    )
    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LIST_INTERESTS)
