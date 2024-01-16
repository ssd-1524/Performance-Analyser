from django.shortcuts import render
from .models import User
# Create your views here.


def user_view(request, emp_id):
    obj = User.objects.get(id=emp_id)
    return render(request, 'index.html', {
        'emp': obj,
    })


def all_emp_view(request):
    arr = User.objects.all()
    return render(request, 'all_emp.html', {
        'arr': arr,
    })
