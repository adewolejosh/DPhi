from django.urls import path
from .views import *


urlpatterns = [
    path('new/', CreateCourses.as_view()),
    path('list/', ListAllCourses.as_view()),
    path('list/<int:id>/', OneCourse.as_view()),
    path('enrol/new/<int:id>/', CourseEnrol.as_view()),
    path('enrol/view/<int:id>/', ViewEnrols.as_view()),
]
