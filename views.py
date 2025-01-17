from django.shortcuts import render, redirect
from .models import Student, Attendance
from datetime import date

# Home page
def home(request):
    return render(request, 'home.html')

# Mark Attendance
def mark_attendance(request):
    students = Student.objects.all()
    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'Absent')
            Attendance.objects.create(student=student, status=status)
        return redirect('view_attendance')
    return render(request, 'mark_attendance.html', {'students': students})

# View Attendance
def view_attendance(request):
    attendance_records = Attendance.objects.filter(date=date.today())
    return render(request, 'view_attendance.html', {'attendance_records': attendance_records})
