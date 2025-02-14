from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Assignment
from .forms import AssignmentForm


class AssignmentListView(View):
    def get(self, request):
        assignments = Assignment.objects.all()
        ctx = {'assignments': assignments}
        return render(request,'assignments/assignments.html', ctx)

class AssignmentCreateView(View):
    def post(self, request):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignments:list')
        ctx = {'form': form}
        return render(request,'assignments/assignments-form.html', ctx)

    def get(self, request):
        form = AssignmentForm()
        ctx = {'form': form}
        return render(request, 'assignments/assignments-form.html', ctx)

class AssignmentUpdateView(View):
    def post(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments:list')
        ctx = {
            'form': form,
            'assignment': assignment,
        }
        return render(request,'assignments/assignments-form.html', ctx)

    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = AssignmentForm(instance=assignment)
        ctx = {
            'form': form,
            'assignment': assignment,
        }
        return render(request, 'assignments/assignments-form.html', ctx)

class AssignmentDeleteView(View):
    def post(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        assignment.delete()
        return redirect('assignments:list')
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        ctx = {'assignment': assignment}
        return render(request,'assignments/delete.html', ctx)
