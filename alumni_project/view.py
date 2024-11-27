
from django.shortcuts import render
from student_app.models import Student
from alumni_app.models import Profile

    
def Home(request):
    total_students = Student.objects.count()
    total_alumnis=Profile.objects.count()
    print("total_students",total_students)
    data={
        "total_students":total_students,
        "total_alumnis":total_alumnis,
    }
    return render(request, 'index1.html',context=data)

def About(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'contact.html')

def jobposts(request):
    return render(request, 'jobposts.html')

def profiles(request):
    return render(request, 'profiles.html')