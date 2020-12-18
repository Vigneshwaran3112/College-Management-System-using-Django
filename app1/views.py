from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import College, Batch, Semester, Department, Section, Designation, Staff, Student, Subject, Mark, Rank

global clg
clg = College.objects.get(id=1)

def Authentication(request):

    if request.method == 'POST':
        user_name = request.POST.get('uname')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        try:
            if password == cpassword:
                USERNAME_FIELD = user_name
                users = User.objects.create_user(USERNAME_FIELD,first_name=first_name,last_name=last_name,email=email,password=password)
                users.is_staff = True
                users.save()
                return render(request, 'home.html', {'user':users})
        except:
            user= User.objects.get(username=user_name)
            msg = 'Username is already exist...'
            return render(request, 'register.html', {'msg':msg})
            
    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            staff = Staff.objects.all()
            student = Student.objects.all()
            sec = Section.objects.all()
            sem = Semester.objects.all()
            batch = Batch.objects.all()
            designation = Designation.objects.values_list('designation')
            des = []
            for i in range(len(designation)):
                des.append(designation[i][0])

            department = Department.objects.values_list('department')
            depart = []
            for i in range(len(department)):
                depart.append(department[i][0])
            return render(request, 'home.html', {'user':user, 'clg':clg, 'des':des, 'department':depart, 'staff':staff, 'student':student, 'sem':sem, 'batch':batch, 'sec':sec})
    return render(request, 'login.html', {'clg':clg})

def logout(request):
    return redirect('/')

def home(request):
    if request.method == 'POST':
        dt = Department.objects.values_list('department')
        d = []
        for i in range(len(dt)):
            d.append(dt[i][0])
        print(d)
        return render(request, 'home.html', {'clg':clg})
    return render(request, 'home.html', {'clg':clg})

def studentlogin(request):
    # d = Department.objects.group_set.all()
    if request.method == 'POST':
        registerno = request.POST.get('registerno')
        name = request.POST.get('studentname')
        s = Student.objects.all()
        m = Mark.objects.all()
        for i in range(5, len(s)+5):
            stud = Student.objects.get(id=i)
            if stud.register_no == registerno:
                m = Mark.objects.all()
                for j in range(1, len(m)+1):
                    mark = Mark.objects.get(student=stud)
                if stud.name == name:
                    print(stud.register_no)
                    print(stud.name)
                    print(stud.department)
                    return render(request, 'studenthome.html', {'user':name, 'clg':clg, 'stud':stud, 'mark':mark})
        return render(request, 'login.html')

def addstaff(request):
    if request.method == 'POST':
        staffid = request.POST.get('staffid')
        staffname = request.POST.get('staffname')
        designation = request.POST.get('designation')
        department = request.POST.get('department')

        sf = Staff.objects.create(staff_id=staffid,name=staffname,designation=designation,department=department)
        st.save()
    return render(request, 'home.html')

def addstudent(request):
    if request.method == 'POST':
        registerno = request.POST.get('registerno')
        studentname = request.POST.get('studentname')
        section = request.POST.get('section')
        department = request.POST.get('department')
        sem = request.POST.get('sem')
        batch = request.POST.get('batch')

        st = Student.objects.create(register_no=registerno, name=studentname, section=section, department=department,sem=sem, batch=batch)
        st.save()
    return render(request, 'home.html')
