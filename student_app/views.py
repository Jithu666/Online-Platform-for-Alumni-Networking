from django.shortcuts import render,redirect,reverse
from . import forms,models
# from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
# from django.conf import settings
# from datetime import date, timedelta
# from quiz import models as QMODEL
# from teacher import models as TMODEL

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

#for showing signup/login button for student
# @login_required(login_url='alumnilogin')
# @user_passes_test(is_student)
def studentclick_view(request):
    # if request.user.is_authenticated:
        # return HttpResponseRedirect('afterlogin')
    return render(request,'students/studentclick.html')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'students/studentsignup.html',context=mydict)



# student_app/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

def student_login_view(request):
    if request.user.is_authenticated:
        return redirect('students:student-dashboard')  # Redirect to a dashboard or homepage if the user is already logged in
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                return HttpResponseRedirect(reverse('students:student-dashboard'))  # Change 'alumni_dashboard' to your desired redirect URL
        else:
            return render(request, 'students/studentlogin.html', {'form': form, 'invalid_creds': True})
    else:
        form = AuthenticationForm()
    
    return render(request, 'students/studentlogin.html', {'form': form})


# class StudentLoginView(LoginView):
#     template_name = 'students/studentlogin.html'

#     def get_success_url(self):
#         return reverse_lazy('students:student-dashboard')  # Ensure this is the name of your dashboard URL pattern

from alumni_app.models import JobListing,Profile
from django.contrib.auth.models import User

# @login_required(login_url='students:studentlogin')
# @user_passes_test(is_student)
def student_dashboard_view(request):
    # print("request.user",request.user)
    # users = User.objects.all()
    job_listings = JobListing.objects.all()
    # return render(request, 'alumni/job_listings.html', {'job_listings': job_listings})

    return render(request, 'students/student_dashboard.html', {'job_listings': job_listings})

# @login_required(login_url='students:studentlogin')
# @user_passes_test(is_student)
def profile_list_view(request):
    profiles = Profile.objects.all()
    print("profiles",profiles)
    # alumni_list = Alumni.objects.all().values('LinkedIn_link')
    # print("alumni_list",alumni_list)
    return render(request, 'students/profile_list.html', {'profiles': profiles})

from django.shortcuts import render, get_object_or_404
# from .models import Profile
from alumni_app.models import Experience, Education, Skill,JobListing,Message
from alumni_app.forms import MessageForm

# @login_required(login_url='students:studentlogin')
# @user_passes_test(is_student)
def profile_detail_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    experiences = Experience.objects.filter(profile=profile)
    educations = Education.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)
    
    return render(request, 'alumni/profile_detail.html', {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    })

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_detail.html', {'messages': messages})

from django.contrib.auth import logout

# @login_required(login_url='students:studentlogin')
# @user_passes_test(is_student)
def logout_view(request):
    logout(request)
    return redirect('Home')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# @login_required(login_url='students:studentlogin')
# @user_passes_test(is_student)
def message_create(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')
        file = request.FILES.get('file')
        username = request.session.get('username')
        if username==None:
            username="admin" 
        
        
        # Assuming 'text' field is required
        if text:
            message = Message.objects.create(text=text, image=image, file=file, user=username)
            return redirect('alumnis:message_list')  # Redirect to message list after successful submission
        else:
            return HttpResponse("Error: Text field is required.")
    else:
        return render(request, 'alumni/send_message.html')


# @login_required(login_url='students:studentlogin')
# @user_passes_test(is_student)
# def message_list(request):
#     messages = Message.objects.all()
#     return render(request, 'students/message_detail.html', {'messages': messages})

def message_list(request):
    # Query the latest messages, ordering by timestamp
    latest_messages = Message.objects.order_by('-timestamp')[:10]  # Fetching latest 10 messages, adjust the number as per your requirement
    
    return render(request, 'students/message_detail.html', {'messages': latest_messages})

from alumni_app.models import Experience, Education, Skill,JobListing,Message,Alumni

def Group_list(request):
    years_of_pass = Alumni.objects.values_list('year_of_pass', flat=True).distinct()
    context = {
        'years_of_pass': years_of_pass,
    }
    return render(request,'students/group_list.html',context)

def year_detail_view(request, year):
    alumni_list = Alumni.objects.filter(year_of_pass=year)
    print("alumni_list",alumni_list)
    context = {
        'year': year,
        'alumni_list': alumni_list,
    }
    return render(request, 'students/year_detail.html', context) 
