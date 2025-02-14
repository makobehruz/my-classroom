from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


from .models import Course
from .forms import CourseForm


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        ctx = {
            'courses': courses,
        }
        return render(request,'courses/courses.html', ctx)

class CourseCreateView(View):
    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
        ctx = {
            'form': form,
        }
        return render(request, 'courses/course-form.html', ctx)

    def get(self, request):
        form = CourseForm()
        ctx = {'form': form}
        return render(request, 'courses/course-form.html', ctx)

class CourseUpdateView(View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
        ctx = {
            'form': form,
            'course': course,
        }
        return render(request, 'courses/course-form.html', ctx)

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(instance=course)
        ctx = {
            'form': form,
            'course': course,
        }
        return render(request, 'courses/course-form.html', ctx)

class CourseDeleteView(View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('courses:list')
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        ctx = {'course': course}
        return render(request,'courses/delete.html', ctx)




