from django import forms
from discoveries.models import PartDiscovered

class f2editForm(forms.Form):
    hostname = forms.CharField(max_length=100)

    supported_parts = PartDiscovered.objects.all()[0:6]
    interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=supported_parts)
#    interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=None)
             
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
