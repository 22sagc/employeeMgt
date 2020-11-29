from django.urls import include, path
from employee import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('employee-registration/', views.employee_registration, name='employee_registration'),
    path('save-employee/', views.save_employee, name='save_employee'),
    path('employee-details/', views.employee_details, name='employee_details'),
    path('edit-employee/<id>/', views.edit_employee, name='edit_employee'),
    path('update-employee/', views.update_employee, name='update_employee'),
    path('delete-employee/', views.delete_employee, name='delete_employee'),

]
