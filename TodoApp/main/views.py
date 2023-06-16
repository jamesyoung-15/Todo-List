from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django import forms

from .models import Task

# Create your views here.

class UserLogin(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(UserLogin, self).get_form(form_class)
        # add placeholder in inputs for styling
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        return form

    # once logged in:
    def get_success_url(self):
        # if sucessful, send user back to tasks lists page
        return reverse_lazy('tasks')

# register user
class RegisterUser(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(RegisterUser, self).get_form(form_class)
        # add placeholder in inputs for styling
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
        return form


    # once valid, login user
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    # redirect user to task list if already logged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUser,self).get(*args, **kwargs)

# show tasks
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks' 

    # only show tasks from user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-task') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context

# show individual task
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'main/task.html'

# edit individual task
class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    # if sucessful, send user back to tasks lists page
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # make sure user is logged in user
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

# update task
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    # if sucessful, send user back to tasks lists page
    success_url = reverse_lazy('tasks')

# delete a task
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'taskdelete'
    template_name = 'main/task_delete.html'
    # if sucessful, send user back to tasks lists page
    success_url = reverse_lazy('tasks')


