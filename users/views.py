from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from assignments.models import Assignment
from courses.models import Course
from .forms import UserForm
from .models import User

class HomeView(View):
    def get(self, request):
        courses = Course.objects.filter(status='ac')
        assignments = Assignment.objects.filter(status='ac')
        users = User.objects.all()
        ctx = {
            'courses': courses,
            'assignments': assignments,
            'users': users,
        }
        return render(request, 'index.html', ctx)


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {
            'users': users,
        }
        return render(request, 'users/users.html', ctx)

class UserCreateView(View):
    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:list')
        ctx = {
            'form': form,
        }
        return render(request, 'users/users-form.html', ctx)

    def get(self, request):
        form = UserForm()
        ctx = {
            'form': form,
        }
        return render(request, 'users/users-form.html', ctx)

class UserUpdateView(View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:list')
        ctx = {
            'form': form,
            'user': user,
        }
        return render(request, 'users/users-form.html', ctx)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        ctx = {
            'form': form,
            'user': user,
        }
        return render(request, 'users/users-form.html', ctx)

class UserDeleteView(View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('users:list')
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        ctx = {
            'user': user,
        }
        return render(request,'users/delete.html', ctx)
