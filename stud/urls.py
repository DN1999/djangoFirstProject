from django.urls import path 
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("student",views.student, name="student"),
    # path("add",views.add,name="add")
    
    path("register",views.register, name="register"),
    path("addStudentPage",views.addStudentPage,name="addStudentPage"),

    path("updateStudent",views.updateStudent, name="updateStudent"),
    path("updateStudentPage",views.updateStudentPage, name="updateStudentPage"),
    path("searchStudent",views.searchStudent, name="searchStudent")
]       