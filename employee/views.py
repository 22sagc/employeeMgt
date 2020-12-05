from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from employee.models import Manager, Employee
from django.contrib.auth.models import User, auth


# Landing Page
def index(request):
    return render(request, 'landing_page.html')


# signup or user create here
@csrf_exempt
def register(request):
    try:
        data = {}
        if request.method == 'POST':
            username = request.POST.get('user_name')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            department = request.POST.get('department')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            # checking both password entries are correct or not
            if password1 == password2:
                # checking user is already exist or not with username
                if User.objects.filter(username=username).exists():
                    data = {'success': 'exist'}
                # checking user is already exist or not with email
                elif User.objects.filter(email=email).exists():
                    data = {'success': 'taken'}
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    manager = Manager.objects.create(name=first_name + ' ' + last_name, email=email,
                                                     department=department)
                    manager.save()
                    data = {'success': 'true'}
            else:
                data = {'success': 'password'}

            return HttpResponse(json.dumps(data), content_type='application/json')

    except Exception:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


# login registered user
@csrf_exempt
def login(request):
    try:
        data = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)
            # checking user is valid or not
            if user is not None:
                auth.login(request, user)
                data = {'success': 'valid'}
            else:
                data = {'success': 'invalid'}
            return HttpResponse(json.dumps(data), content_type='application/json')

    except Exception:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


# logout user
@csrf_exempt
def logout(request):
    try:
        data = {}
        # logout code
        auth.logout(request)
        return redirect('/')  # redirect to home page

    except Exception:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


# displaying user form
def employee_registration(request):
    return render(request, 'employee_registration.html')


# employee registration
@csrf_exempt
def save_employee(request):
    try:
        data = {}
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            department = request.POST.get('department')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')

            # checking employee is already registered with this email id or not
            if Employee.objects.filter(email=email).exists():
                data = {'success': 'exist'}
            else:
                # attaching login manager foreign key in employee table
                manager_ref = Manager.objects.get(email=request.user.email)
                employee = Employee.objects.create(manager_id=manager_ref, first_name=first_name, last_name=last_name,
                                                   email=email,
                                                   mobile=mobile, department=department, city=city)
                employee.save()
                data = {'success': 'true'}

    except Exception:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


# get employee details in datatable manager wise added manager foreign key
@csrf_exempt
def employee_details(request):
    # getting values for logged in managers employees only
    manager_ref = Manager.objects.get(email=request.user.email)
    employeeObj = Employee.objects.filter(is_deleted=False, manager_id__id=manager_ref.id).order_by('first_name',
                                                                                                    'last_name')  # sorted by first and last name
    data = {'employeeObj': employeeObj}
    return render(request, 'employee_details.html', data)


# get for to edit employee details
def edit_employee(request, id):
    employeeObj = Employee.objects.get(id=id)
    data = {'employeeObj': employeeObj}
    return render(request, 'edit_employee.html', data)


# update employee
@csrf_exempt
def update_employee(request):
    try:
        data = {}
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            department = request.POST.get('department')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')
            emp_id = request.POST.get('emp_id')
            Employee.objects.filter(id=emp_id).update(first_name=first_name, last_name=last_name,
                                                      mobile=mobile, department=department, city=city)
            data = {'success': 'true'}

    except Exception:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


# delete employee, not hard deleting entry just enable disable using is_deleted flag
@csrf_exempt
def delete_employee(request):
    try:
        data = {}
        if request.method == 'POST':
            emp_id = request.POST.get('emp_id')
            Employee.objects.filter(id=emp_id).update(
                is_deleted=True)  # changing flag True or false, True means deleted and False means not deleted
            data = {'success': 'true'}

    except Exception:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')
