from socket import fromshare
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.hashers import check_password
from django.db.models import Q


class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields=('email','firstname','lastname','username','address','role','image')
  
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields=('email','firstname','lastname','username','address','role','image')

class CustomUserLoginForm(forms.Form):

  username = forms.CharField(max_length=CustomUser._meta.get_field('email').max_length)
  password = forms.CharField(min_length=6, max_length=16, widget=forms.PasswordInput())
 
  def is_valid(self, cate):
    valid = super(CustomUserLoginForm, self).is_valid()
    if not valid:
      return valid
    try:
      user = CustomUser.objects.get(
        Q(email=self.cleaned_data['username']) & Q(role=cate)
      )
    except CustomUser.DoesNotExist:
      self._errors['no_user'] = 'User does not exist'
      return False
    if not check_password(self.cleaned_data['password'], user.password):
      self._errors['invalid_password'] = 'Password is invalid'
      return False
    if not user.role==cate:
      self._error['access_denied'] = 'Access Denied'
      return False
    return True

