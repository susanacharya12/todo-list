from django.urls import path
from .views import (
    student_list,
    student_retrived,
    student_create,
    update_student,
    delete_student,
)

urlpatterns = [
    # List all students
    path('students/', student_list, name='student-list'),

    # Retrieve a single student by id
    path('students/<int:pk>/', student_retrived, name='student-detail'),

    # Create a student
    path('students-create/', student_create, name='student-create'),

    # Update a student
    path('students-update/<int:pk>/', update_student, name='student-update'),

    # Delete a student
    path('students-delete/<int:pk>/', delete_student, name='student-delete'),
]
