from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomUserChangeForm,CustomUserLoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django .urls import reverse_lazy

def index(request):
  return render(request,'index.html')

def signup(request):
  form = CustomUserCreationForm()
  if (request.method=='POST'):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form .save()
    messages.error(request, "Unsuccessful registration. Invalid information.")
  return render(request,'signup.html',{'form':form})

def user_login(request):
  if request.method == "POST":
    print(request.POST)
    form = CustomUserLoginForm(request.POST)
    if form.is_valid(request.POST.get('category')):
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      category = request.POST.get('category')
      user = authenticate(email=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return render(request,'blog.html',context = {'username':username,'role':category})
      else:
        messages.error(request,"Invalid username or password.")
    else:
      print("done")
      messages.error(request,"Invalid username or password.")
  form = AuthenticationForm()
  return render(request=request, template_name="login.html", context={"login_form":form})

def user_logout(request):
    logout(request)
    return redirect('index')



class BlogCreate(LoginRequiredMixin,CreateView):
  model = Blog
  fields = ['title','content']
  success_url = reverse_lazy('task')
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(BlogCreate,self).form_valid(form)