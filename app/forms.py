from django import forms
from django.forms import inlineformset_factory, ModelForm

from .models import Author, Blog, FamilyMember,Profile


class FamilyMemberForm(ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()

FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
                                            form=FamilyMemberForm, extra=3)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'id': "exampleInputEmail1",
                       "placeholder": "Enter name"}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', "id": "exampleInputName",
                       "placeholder": "Enter email"}
            )
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'date']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'id': "exampleInputTitle",
                       "placeholder": "Enter title"}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', "id": "exampleFormControlTextarea1",
                       "placeholder": "Enter description"}
            ),
            'date': forms.TextInput(
                attrs={'class': 'form-control', "id": "exampleInputDate",
                       "placeholder": "01/01/2024", "type": "date"
                       }
            )
        }