from django.shortcuts import render,redirect
from  employee.models import EmployeeModel
from employee.forms import EmployeeForm
from employee.forms import SignupForm
from employee.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate




def Signup(request):                                                                #insert data in database

    message = ""
    Form = SignupForm()
    if request.method == 'POST':
        Form = SignupForm(request.POST)
        if Form.is_valid():
            formData = Form.cleaned_data
            user = User()
            user.username = formData['username']
            user.set_password(formData['password'])  # password hasing done here
            user.save()
            message = 'Registration done sucessfully,Thank You'
            return redirect(signin)
    return render(request, 'signup.html', {'formm': Form, 'message': message})




def signin(request):                                                  #Login authentication(login must be diff from inbuild login)
    if request.user.username:
        return redirect(index)

    obj=LoginForm()
    isValidUser=""
    if request.method=='POST':
        obj=LoginForm(request.POST)
        if obj.is_valid():
            username=obj.cleaned_data['username']
            password=obj.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is None:
                isValidUser='Invalid login details!'
            else:
                login(request,user)
                return redirect(index)
    return render(request,'login.html',{'form':obj,'isValidUser':isValidUser})



def create(request):                                               #create table using POST method
    empForm = EmployeeForm()
    if request.method == 'POST':
        empForm = EmployeeForm(request.POST)
        if empForm.is_valid():
            empModel = EmployeeModel()
            empModel.emp_Firstname = empForm.cleaned_data['emp_Firstname']
            empModel.emp_lastname = empForm.cleaned_data['emp_lastname']
            empModel.emp_Address = empForm.cleaned_data['emp_Address']
            empModel.emp_DOB = empForm.cleaned_data['emp_DOB']
            empModel.emp_Mobilenumber=empForm.cleaned_data['emp_Mobilenumber']
            empModel.emp_city = empForm.cleaned_data['emp_city']
            empModel.save()
            return redirect(index)
    return render(request, 'CRUD/create.html', {'empForm': empForm})           #Acess of the values using keys and value


def index(request):                                                              #retriving the data
    resultset = EmployeeModel.objects.all()
    return render(request, 'CRUD/index.html', {'data': resultset})

def update(request):                                                             # for update data post method
    id = request.GET['id']                                                        #update data of selected id
    result = EmployeeModel.objects.get(id=id)
    empForm = EmployeeForm(instance=result)
    if request.method == 'POST':
        empForm = EmployeeForm(request.POST, instance=result)
        if empForm.is_valid():
            empModel = EmployeeModel()
            empModel.id = id                                                         #it is for update the details as per selected id
            empModel.emp_Firstname = empForm.cleaned_data['emp_Firstname']
            empModel.emp_lastname = empForm.cleaned_data['emp_lastname']
            empModel.emp_Address = empForm.cleaned_data['emp_Address']
            empModel.emp_DOB= empForm.cleaned_data['emp_DOB']
            empModel.emp_Mobilenumber = empForm.cleaned_data['emp_Mobilenumber']
            empModel.emp_city = empForm.cleaned_data['emp_city']
            empModel.save()
            return redirect(index)
    return render(request, 'CRUD/update.html', {'empForm': empForm})


def delete(request):                                                                  # delete data of selected id
    id = request.GET['id']
    result = EmployeeModel.objects.get(id=id)
    result.delete()
    return redirect(index)

def dashBoard(request):                                                              #showing information
    return render(request,'dashboard.html')

def Logout(request):                                                                  #Logout
    logout(request)
    return redirect(signin)

