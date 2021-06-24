from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields ='__all__' # Set the fields attribute to the special value '__all__' to indicate that all fields in the model should be used.
        # labels = {
        #     'fullname':'Full Name',
        #     'emp_code':'EMP. Code'
        # }

    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm,self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = "Select"
    #     self.fields['emp_code'].required = False