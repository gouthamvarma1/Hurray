from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile  


class ExtendedUserCreationForm(UserCreationForm):
    username=forms.CharField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user




class UserProfileForm(forms.ModelForm):
    organization_name=forms.CharField(required=True)
    class Meta:
        model=UserProfile
        fields=("organization_name", )


    def save(self, commit=True):
        userprofile=super().save(commit=False)
        userprofile.organization_name = self.cleaned_data["organization_name"]
        if commit:
            userprofile.save()
        return userprofile
