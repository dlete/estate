from django import forms
from support.models import PartSupported

class EditPartSupportedForm(forms.Form):
    project = forms.CharField(max_length=100)
    budget_name = forms.CharField(max_length=100)

    '''
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = PartSupported
    '''
