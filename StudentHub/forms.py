from django import forms 

from StudentHub.models import Category, Student


class CategoryForm(forms.ModelForm):

    category_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    
    class Meta:

        model = Category

        fields = ["id", "category_name"]

        widgets = {
            "category_name": forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Type category...'}),          
        }



class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ["id", "student_name", "category_name", "mobile_number", "place", "email", "qualification"]

    
        widgets = {
            "student_name": forms.TextInput(attrs={'class': 'form-control mb-3'}),
            "category_name": forms.Select(attrs={'class': 'form-select mb-3'}),
            "mobile_number": forms.TextInput(attrs={'class': 'form-control mb-3'}),
            "place": forms.TextInput(attrs={'class': 'form-control mb-3'}),
            "email": forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            "qualification": forms.TextInput(attrs={'class': 'form-control mb-3'})
            
        }

        

        

