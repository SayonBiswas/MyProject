from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Max
from .models import Student

# 🏠 Home Page
def index(request):
    return render(request, 'students/index.html')


# ➕ Add Student
def add_student(request):
    if request.method == "POST":
        adm = int(request.POST['admission_number'])
        nm = request.POST['name']
        rl = int(request.POST['roll_number'])
        cl = int(request.POST['student_class'])
        sec = request.POST['section']
        phy = int(request.POST['physics'])
        chem = int(request.POST['chemistry'])
        math = int(request.POST['maths'])
        comp = int(request.POST['computer'])
        eng = int(request.POST['english'])

        total = phy + chem + math + comp + eng
        avg = total / 5
        per = avg

        # Grade logic
        if per >= 90:
            grade = 'A+'
        elif per >= 80:
            grade = 'A'
        elif per >= 70:
            grade = 'B'
        elif per >= 60:
            grade = 'C'
        elif per >= 50:
            grade = 'D'
        else:
            grade = 'F'

        result = 'Pass' if per >= 40 else 'Fail'

        Student.objects.create(
            admission_number=adm,
            name=nm,
            roll_number=rl,
            student_class=cl,
            section=sec,
            physics=phy,
            chemistry=chem,
            maths=math,
            computer=comp,
            english=eng,
            total=total,
            average=avg,
            percentage=per,
            grade=grade,
            result=result
        )
        return render(request, 'students/success.html')
    return render(request, 'students/add_student.html')


# 📋 View All Students
def view_students(request):
    students = Student.objects.all().order_by('admission_number')
    return render(request, 'students/view_students.html', {'students': students})


# 🔍 Search Student by Admission Number or Name
def search_student(request):
    query = request.GET.get('query')
    students = []
    if query:
        students = Student.objects.filter(name__icontains=query) | Student.objects.filter(admission_number__icontains=query)
    return render(request, 'students/search_student.html', {'students': students, 'query': query})


# ✏️ Update Student Record
def update_student(request, admission_number):
    student = get_object_or_404(Student, pk=admission_number)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll_number = int(request.POST['roll_number'])
        student.student_class = int(request.POST['student_class'])
        student.section = request.POST['section']
        student.physics = int(request.POST['physics'])
        student.chemistry = int(request.POST['chemistry'])
        student.maths = int(request.POST['maths'])
        student.computer = int(request.POST['computer'])
        student.english = int(request.POST['english'])

        total = student.physics + student.chemistry + student.maths + student.computer + student.english
        student.total = total
        student.average = total / 5
        student.percentage = student.average

        if student.percentage >= 90:
            student.grade = 'A+'
        elif student.percentage >= 80:
            student.grade = 'A'
        elif student.percentage >= 70:
            student.grade = 'B'
        elif student.percentage >= 60:
            student.grade = 'C'
        elif student.percentage >= 50:
            student.grade = 'D'
        else:
            student.grade = 'F'

        student.result = 'Pass' if student.percentage >= 40 else 'Fail'
        student.save()
        return redirect('view_students')
    return render(request, 'students/update_student.html', {'student': student})


# 🗑️ Delete Student Record
def delete_student(request, admission_number):
    student = get_object_or_404(Student, pk=admission_number)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    return render(request, 'students/delete_student.html', {'student': student})


# 🏆 Display Topper(s)
def topper(request):
    top_score = Student.objects.aggregate(Max('percentage'))['percentage__max']
    toppers = Student.objects.filter(percentage=top_score)
    return render(request, 'students/topper.html', {'toppers': toppers, 'top_score': top_score})
