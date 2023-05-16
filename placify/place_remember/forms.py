from django import forms


class MemoryForm(forms.Form):
    title = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    comment = forms.CharField(widget=forms.Textarea)
    latitude = forms.FloatField(widget=forms.HiddenInput)
    longitude = forms.FloatField(widget=forms.HiddenInput)
