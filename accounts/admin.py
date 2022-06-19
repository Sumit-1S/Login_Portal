from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ('email','is_staff','is_active','firstname','lastname',)
  list_filter = ('email','is_staff','is_active',)
  fieldsets = (
    (None,{'fields':('email','password','firstname','lastname','username','address','role','image')}),
    ('permissions',{'fields':('is_staff','is_active')}),
  )
  add_fieldsets = (
    (None,{
      'classes':('wide',),
      'fields':('firstname','lastname','username','address','role','email','password1','password2','image','is_staff','is_active')
    }),
  )
  search_fields = ('email',)
  ordering = ('email',)

# admin.site.unregister(User)
admin.site.register(CustomUser,CustomUserAdmin)