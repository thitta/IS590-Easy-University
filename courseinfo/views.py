from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View

from .models import Instructor, Section, Course, Semester, Student, Registration


class CourseDetail(View):

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        section_list = course.sections.all()
        context = {
            "course": course,
            "section_list": section_list
        }
        return render_to_response(template_name="courseinfo/course_detail.html", context=context)


class CourseList(View):

    def get(self, request):
        return render(
            request,
            template_name="courseinfo/course_list.html",
            context={"course_list": Course.objects.all()}
        )


class InstructorDetail(View):

    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        section_list = instructor.sections.all()
        context = {
            "instructor": instructor,
            "section_list": instructor.sections.all(),
        }
        return render_to_response(template_name="courseinfo/instructor_detail.html", context=context)


class InstructorList(View):

    def get(self, request):
        return render(
            request,
            template_name="courseinfo/instructor_list.html",
            context={"instructor_list": Instructor.objects.all()}
        )


class RegistrationDetail(View):

    def get(self, request, pk):
        registration = get_object_or_404(Registration, pk=pk)
        context = {
            "registration": registration,
            "student": registration.student,
            "section": registration.section,
        }
        return render_to_response(template_name="courseinfo/registration_detail.html", context=context)


class RegistrationList(View):

    def get(self, request):
        return render(
            request,
            template_name="courseinfo/registration_list.html",
            context={"registration_list": Registration.objects.all()}
        )


class SectionDetail(View):

    def get(self, request, pk):
        section = get_object_or_404(Section, pk=pk)
        context = {
            "section": section,
            "semester": section.semester,
            "course": section.course,
            "instructor": section.instructor,
            "registration_list": section.registrations.all(),
        }
        return render_to_response(template_name="courseinfo/section_detail.html", context=context)


class SectionList(View):

    def get(self, request):
        return render(
            request,
            template_name="courseinfo/section_list.html",
            context={"section_list": Section.objects.all()}
        )


class SemesterDetail(View):

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        context = {
            "semester": semester,
            "semester_name": semester.semester_name,
        }
        return render_to_response(template_name="courseinfo/semester_detail.html", context=context)


class SemesterList(View):

    def get(self, request):
        return render(
            request,
            template_name="courseinfo/semester_list.html",
            context={"semester_list": Semester.objects.all()}
        )


class StudentDetail(View):

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        registration_list = student.registrations.all()
        context = {
            "student": student,
            "registration_list": registration_list
        }
        return render_to_response(template_name="courseinfo/student_detail.html", context=context)


class StudentList(View):

    def get(self, request):
        return render(
            request,
            template_name="courseinfo/student_list.html",
            context={"student_list": Student.objects.all()}
        )
