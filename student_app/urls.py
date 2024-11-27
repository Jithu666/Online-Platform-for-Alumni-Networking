from django.urls import path
from student_app import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
path('studentclick', views.studentclick_view,name='studentclick'),
path('studentlogin', views.student_login_view, name='studentlogin'),
# path('studentlogin', LoginView.as_view(template_name='students/studentlogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view,name='studentsignup'),
path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
path('profile_list_view/', views.profile_list_view, name='profile_list_view'),
path('profile_detail_view/<int:profile_id>/', views.profile_detail_view, name='profile_detail_view'),
path("message_list",views.message_list,name="message_list"),
path("logout_view",views.logout_view,name="logout_view"),
path('create/', views.message_create, name='message_create'),
    # path('message_list/', views.message_list, name='message_list'),
path('message_list/', views.message_list, name='message_list'),
path("Group_list",views.Group_list,name='Group_list'),
path('year-detail/<int:year>/', views.year_detail_view, name='year_detail_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)