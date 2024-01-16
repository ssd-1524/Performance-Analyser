from django import forms
from .models import User


class TeamLeadInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'Emp_id': 'Employee ID',
            'Position': 'Position',
            'Department': 'Department',
            'Grade': 'Grade',
            'Badges': 'Badges',
        }
