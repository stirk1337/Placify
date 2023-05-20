from django import forms


class MemoryForm(forms.Form):
    title = forms.CharField(label='Название', max_length=255)
    comment = forms.CharField(label='Описание', widget=forms.Textarea)
    latitude = forms.FloatField(widget=forms.HiddenInput)
    longitude = forms.FloatField(widget=forms.HiddenInput)
