"""IIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('attendance/',views.attendance,name='attendance'),
    path('LeaveRecord/', views.leaveRecord, name ='LeaveRecord'),
    path('Task/', views.task, name='Task'),
    path('login/',views.my_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('logout/',views.my_logout,name='logout'),
    path('attn_edit/<int:id>',views.attn_edit,name='attn_edit'),
    path('attendance/delete/<int:id>',views.attn_delete,name='attn_delete'),
    path('task_edit/<int:id>',views.task_edit,name='task_edit'),
    path('task/delete/<int:id>',views.task_delete,name='task_delete'),
    path('leave_edit/<int:id>',views.leave_edit,name='leave_edit'),
    path('LeaveRecord/delete/<int:id>',views.leave_delete,name='leave_delete'),
    path('blog/',views.blog,name='blog'),
    path('Comment/',views.Comment,name='Comment'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
