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

    # http://devdens.blogspot.ie/2014/04/django-multiple-choice-field-and-how-to.html
    # what is a static choices variable?
    # this works, if the list is set as a "static variable" (whatever that is!)
    LIST_INTERESTS = [[p.id, p.serial_number] for p in PartDiscovered.objects.all()[0:4]]

# both work!
#    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LIST_INTERESTS)
    interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=PartDiscovered.objects.all()[0:4])
