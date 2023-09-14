from django import forms


class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder" : "Enter a title"
            }
        )
    )
    
    link = forms.URLField() 
    
    description = forms.CharField(widget=forms.Textarea)