from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee.first_name = form.cleaned_data['first_name']
            employee.last_name = form.cleaned_data['last_name']
            employee.department = form.cleaned_data['department']
            employee.designation = form.cleaned_data['designation']
            employee.date_of_joining = form.cleaned_data['date_of_joining']
            employee.salary = form.cleaned_data['salary']
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(initial={
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'department': employee.department,
            'designation': employee.designation,
            'date_of_joining': employee.date_of_joining,
            'salary': employee.salary,
        })
    
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')
