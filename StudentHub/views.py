from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from StudentHub.models import Category, Student
from StudentHub.forms import CategoryForm, StudentForm

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):

        cat_form = CategoryForm()
        categories = Category.objects.all()
        students = Student.objects.all()

        return render(request, "index.html", {"categories": categories, "students": students, 'cat_form': cat_form})

    def post(self, request, *args, **kwargs):

        cat_form = CategoryForm()
        categories = Category.objects.all()
        students = Student.objects.all()

        if "category_name" in request.POST:

            cat_form = CategoryForm(request.POST)
            
            if cat_form.is_valid():
                cat_form.save()
                messages.success(request, "New category added successfully.")
                return redirect('home')
            
        if "category" in request.POST:

            if request.POST.get('category') == "all":
                students = Student.objects.all()
                return redirect('home')
            
            category_id = request.POST.get("category")
            category_obj = Category.objects.get(id=category_id)
            students = Student.objects.filter(category_name=category_obj)

        return render(request, "index.html", {"categories": categories, "students": students, 'cat_form': cat_form})

class CatFormView(View):

    def get(self, request, *args, **kwargs):

        cat_form = CategoryForm()

        return render(request, "cat_form.html", {"cat_form": cat_form})

    def post(self, request, *args, **kwargs):

        cat_form = CategoryForm(request.POST)

        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, "New category added successfully.")
            return redirect("home")
        
        return render(request, "cat_form.html", {"cat_form": cat_form})

class StuFormView(View):

    def get(self, request, *args, **kwargs):

        stu_form = StudentForm()
        return render(request, "stu_form.html", {"stu_form": stu_form})

    def post(self, request, *args, **kwargs):

        stu_form = StudentForm(request.POST)

        if stu_form.is_valid():
            stu_form.save()
            messages.success(request, "New student added successfully.")
            return redirect("home")
        
        return render(request, "stu_form.html", {"stu_form": stu_form})

class StudentDetailView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')
        qs = Student.objects.get(id=id)

        return render(request, 'student_detail.html', {'data': qs})

class StudentDeleteView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')
        Student.objects.get(id=id).delete()
        messages.success(request, "Student deleted successfully.")

        return redirect('home')

class StudentUpdateView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')
        student_object = Student.objects.get(id=id)
        form = StudentForm(instance=student_object)

        return render(request, 'student_edit.html', {'form': form})

    def post(self, request, *args, **kwargs):

        id = kwargs.get('pk')
        student_object = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=student_object)

        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated successfully.")
            return redirect('home')
        else:
            return render(request, 'student_edit.html', {'form': form})
