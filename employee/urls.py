from django.urls import include, path
from employee import views, api

urlpatterns = [

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('saveEmpApi/', api.saveEmp, name='saveEmpApi'),
    path('showEmpApi/', api.showEmp, name='showEmpApi'),
    path('saveUserApi/', api.saveUser, name='saveUserApi'),
    path('saveMangerApi/', api.saveManager, name='saveMangerApi'),

    # class
    path('employeeDetails/', views.employeeDetails.as_view(), name='employeeDetails'),
    path('employee/', views.employee.as_view(), name='employee'),
    path('saveEditEmpApi/<int:pk>', api.saveEmployeeApi.as_view(), name='employee'),
    path('updateEmployee/<int:pk>', views.updateEmployee.as_view(), name='updateEmployee'),
    path('delete-employee/', views.delete_employee, name='delete_employee'),

]
