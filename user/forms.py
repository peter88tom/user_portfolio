from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
  username = forms.CharField(max_length=200, required=True)
  password1 = forms.CharField(max_length=200, required=True)
  password2 = forms.CharField(max_length=200, required=True)

  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError(f"The two password fields does not match")
    return password2

