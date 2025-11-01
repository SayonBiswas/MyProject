from django.shortcuts import render, redirect
from .models import Student

def index(request):
    return render(request, 'students/index.html')

def add_student(request):
    if request.method == 'POST':
        adm = int(request.POST['admission_number'])
        name = request.POST['name']
        roll = int(request.POST['roll_number'])
        cl = int(request.POST['class'])
        sec = request.POST['section']
        phy = int(request.POST['physics'])
        chem = int(request.POST['chemistry'])
        math = int(request.POST['mathematics'])
        comp = int(request.POST['computer'])
        eng = int(request.POST['english'])
        
        total = phy + chem + math + comp + eng
        avg = total / 5
        per = avg
        
        Student.objects.create(
            admission_number = adm, name = name, roll_number = roll, class_name = cl, section = sec, physics = phy, chemistry = chem,
            mathematics = math, computer = comp, english = eng, total = total, average = avg, percentage = per
        )
        return render(request, 'students/success.html', {'name': name})
    return render(request, 'students/add_student.html')

def view_all(request):
    students = Student.objects.all()
    return render(request, 'students/view_all.html', {'students': students})
