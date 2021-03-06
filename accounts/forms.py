from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields=('email','firstname','lastname','username','address','role','image')
  
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields=('email','firstname','lastname','username','address','role','image')