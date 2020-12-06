from django.shortcuts import render, redirect
import json, requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from employee.models import Manager, Employee
from django.contrib.auth.models import User, auth
from django.views import View


# Landing Page
class landing(View):
    def get(self, request):
        return render(request, 'landing_page.html')

    def post(self, request):
        headers = {'Content-Type': 'application/json'}
        if request.method == 'POST':
            username = request.POST.get('user_name')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            department = request.POST.get('department')
            password = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if User.objects.filter(username=username).exists():
                data = {'success': 'exist'}
            elif User.objects.filter(email=email).exists():
                data = {'success': 'taken'}
            elif password != password2:
                data = {'success': 'password'}
            else:
                data = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email,
                        'department': department, 'password': password,
                        'name': first_name + ' ' + last_name,
                        'success': 'true'}
                print(data)
                requests.post('http://127.0.0.1:8000/employee/saveUserApi/', json=data, headers=headers)
                requests.post('http://127.0.0.1:8000/employee/saveMangerApi/', json=data, headers=headers)

        else:
            data = {'success': 'false'}
        return HttpResponse(json.dumps(data), headers)


class employee(View):
    def get(self, request):
        return render(request, 'employee_registration.html')

    def post(self, request):
        headers = {'Content-Type': 'application/json'}
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            department = request.POST.get('department')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')
            manager = Manager.objects.get(email=request.user.email)
            manager_id = manager.id

            if Employee.objects.filter(email=email).exists():
                data = {'success': 'exist'}
            else:
                data = {'first_name': first_name, 'last_name': last_name, 'email': email,
                        'department': department, 'mobile': mobile, 'city': city, 'manager_id': manager_id,
                        'success': 'true'}

                requests.post('http://127.0.0.1:8000/employee/saveEmpApi/', json=data, headers=headers)
        else:
            data = {'success': 'false'}
        return HttpResponse(json.dumps(data), headers)


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


# display employee deatils
class employeeDetails(View):
    def get(self, request):
        # getting values for logged in managers employees only
        manager_ref = Manager.objects.get(email=request.user.email)
        employeeObj = Employee.objects.filter(is_deleted=False, manager_id__id=manager_ref.id).order_by('first_name',
                                                                                                        'last_name')  # sorted by first and last name
        data = {'employeeObj': employeeObj}
        return render(request, 'employee_details.html', data)


class updateEmployee(View):
    def get(self, request, pk):
        employeeObj = Employee.objects.get(id=pk)
        data = {'employeeObj': employeeObj}
        return render(request, 'edit_employee.html', data)

    def post(self, request):
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
