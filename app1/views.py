from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *

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
                return redirect('/login/')
        except:
            user= User.objects.get(username=user_name)
            msg = 'Username is already exist...'
            return render(request, 'register.html', {'msg':msg})
            
    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        global username, password
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            staff = Staff.objects.all()
            student = Student.objects.all()
            sec = Section.objects.all()
            sem = Semester.objects.all()
            batch = Batch.objects.all()
            des = Designation.objects.all()
            depart = Department.objects.all()
            subject = Subject.objects.all()
            mark = Mark.objects.all()
            return render(request, 'home.html', {'user':user, 'clg':clg, 'des':des,'mark':mark, 'subject':subject,'department':depart, 'staff':staff, 'student':student, 'sem':sem, 'batch':batch, 'sec':sec})
    return render(request, 'login.html', {'clg':clg})

def logout(request):
    return redirect('/')

def home(request):
    user = authenticate(username=username, password=password)
    if user.is_authenticated:
        staff = Staff.objects.all()
        student = Student.objects.all()
        sec = Section.objects.all()
        sem = Semester.objects.all()
        batch = Batch.objects.all()
        des = Designation.objects.all()
        depart = Department.objects.all()
        subject = Subject.objects.all()
        mark = Mark.objects.all()
        return render(request, 'home.html', {'user':user, 'clg':clg, 'des':des,'mark':mark,'subject':subject, 'department':depart, 'staff':staff, 'student':student, 'sem':sem, 'batch':batch, 'sec':sec})
    return render(request, 'login.html', {'clg':clg})

def studentlogin(request):
    # d = Department.objects.group_set.all()
    if request.method == 'POST':
        registerno = request.POST.get('registerno')
        name = request.POST.get('studentname')
        s = Student.objects.all()
        m = Mark.objects.all()
        r = Rank.objects.all()
        for i in range(5, len(s)+5):
            stud = Student.objects.get(id=i)
            if stud.register_no == registerno:
                m = Mark.objects.all()
                for j in range(1, len(m)+1):
                    mark = Mark.objects.get(student=stud)
                for k in range(1, len(r)+1):
                    rank = Rank.objects.get(student=stud)
                if stud.name == name:
                    return render(request, 'studenthome.html', {'user':name, 'clg':clg, 'stud':stud, 'mark':mark, 'rank':rank})
    return render(request, 'login.html')

def editmark(request, id):
    if request.method == 'POST':
        sem = request.POST.get('sem')
        registerno = request.POST.get('registerno')
        subject = request.POST.get('subject')
        department = request.POST.get('department')
        mark = request.POST.get('mark')
        department = Department.objects.get(id=department)
        sem = Semester.objects.get(id=sem)
        subject = Subject.objects.get(id=subject)
        m = Mark.objects.get(id=id)
        m.sem = sem
        m.register_no = registerno
        m.subject = subject
        m.department = department
        m.mark = mark
        m.save()
        return redirect('/home/')

def addmark(request):
    if request.method == 'POST':
        sem = request.POST.get('sem')
        registerno = request.POST.get('registerno')
        subject = request.POST.get('subject')
        department = request.POST.get('department')
        mark = request.POST.get('mark')
        department = Department.objects.get(id=department)
        sem = Semester.objects.get(id=sem)
        subject = Subject.objects.get(id=subject)
        m = Mark.objects.create(sem=sem, register_no=registerno,subject=subject, department=department, mark=mark)
        m.sava()
        return redirect('/home/')

def addstaff(request):
    if request.method == 'POST':
        staffid = request.POST.get('staffid')
        staffname = request.POST.get('staffname')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        designation = Designation.objects.get(id=designation)
        department = Department.objects.get(id=department)
        sf = Staff.objects.create(staff_id=staffid,name=staffname,designation=designation,department=department)
        sf.save()
    return redirect('/home/')

def addstudent(request):
    if request.method == 'POST':
        registerno = request.POST.get('registerno')
        studentname = request.POST.get('studentname')
        section = request.POST.get('section')
        department = request.POST.get('department')
        sem = request.POST.get('sem')
        batch = request.POST.get('batch')
        section = Section.objects.get(id=section)
        department = Department.objects.get(id=department)
        sem = Semester.objects.get(id=sem)
        batch = Batch.objects.get(id=batch)
        st = Student.objects.create(register_no=registerno, name=studentname, section=section, department=department,sem=sem, batch=batch)
        st.save()
    return redirect('/home/')

def deletestaff(request, id):
    st = ''
    st = Staff.objects.get(id=id)
    st.delete()
    return redirect('/home/')

def editstaff(request, id):
    editsf = ''
    editsf = Staff.objects.get(id=id)
    staff = 'block'
    student = 'none'
    des = Designation.objects.all()
    depart = Department.objects.all()
    return render(request, 'update.html', {'user':username, 'clg':clg, 'editstaff':editsf, 'staffpage':staff, 'studentpage':student, 'des':des, 'department':depart})

def updatestaff(request, id):
    if request.method == 'POST':
        staff_id = request.POST.get('staffid')
        name = request.POST.get('staffname')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        designation = Designation.objects.get(id=designation)
        department = Department.objects.get(id=department)
        sf = Staff.objects.get(id=id)
        sf.staff_id = staff_id
        sf.name = name
        sf.designation = designation
        sf.department = department
        sf.save()
        return redirect('/home/')

def deletestudent(request, id):
    st = ''
    st = Student.objects.get(id=id)
    st.delete()
    return redirect('/home/')

def editstudent(request, id):
    editst = ''
    editst = Student.objects.get(id=id)
    staff = 'none'
    student = 'block'
    sec = Section.objects.all()
    sem = Semester.objects.all()
    batch = Batch.objects.all()
    depart = Department.objects.all()
    return render(request, 'update.html', {'user':username, 'clg':clg, 'editstudent':editst, 'staffpage':staff, 'studentpage':student, 'department':depart, 'sem':sem, 'batch':batch, 'sec':sec})

def updatestudent(request, id):
    if request.method == 'POST':
        registerno = request.POST.get('registerno')
        name = request.POST.get('studentname')
        section = request.POST.get('section')
        department = request.POST.get('department')
        sem = request.POST.get('sem')
        batch = request.POST.get('batch')
        section = Section.objects.get(id=section)
        department = Department.objects.get(id=department)
        sem = Semester.objects.get(id=sem)
        batch = Batch.objects.get(id=batch)
        st = Student.objects.get(id=id)
        st.register_no = registerno
        st.name = name
        st.section = section
        st.department = department
        st.sem = sem
        st.batch = batch
        st.save()
        return redirect('/home/')

