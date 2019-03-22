from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from courseinfo.forms import CourseForm, InstructorForm, SectionForm, SemesterForm, StudentForm, RegistrationForm
from .models import Instructor, Section, Course, Semester, Student, Registration
from .utils import PageLinksMixin


class CourseDetail(View):

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        section_list = course.sections.all()
        context = {
            "course": course,
            "section_list": section_list
        }
        return render(request,
                      template_name="courseinfo/course_detail.html",
                      context=context)


class CourseList(ListView):
    model = Course


class CourseCreate(CreateView):
    form_class = CourseForm
    model = Course


class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = "courseinfo/course_form_update.html"


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy("courseinfo_course_list_urlpattern")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"course": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/course_refuse_delete.html", context)


class InstructorDetail(View):

    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        context = {
            "instructor": instructor,
            "section_list": instructor.sections.all(),
        }
        return render(request,
                      template_name="courseinfo/instructor_detail.html",
                      context=context)


class InstructorList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor


class InstructorCreate(CreateView):
    form_class = InstructorForm
    model = Instructor


class InstructorUpdate(UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = "courseinfo/instructor_form_update.html"


class InstructorDelete(DeleteView):
    model = Instructor
    success_url = reverse_lazy("courseinfo_instructor_list_urlpattern")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"instructor": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/instructor_refuse_delete.html", context)


class RegistrationDetail(View):

    def get(self, request, pk):
        registration = get_object_or_404(Registration, pk=pk)
        context = {
            "registration": registration,
            "student": registration.student,
            "section": registration.section,
        }
        return render(request,
                      template_name="courseinfo/registration_detail.html",
                      context=context)


class RegistrationList(ListView):
    model = Registration


class RegistrationCreate(CreateView):
    form_class = RegistrationForm
    model = Registration


class RegistrationUpdate(UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = "courseinfo/registration_form_update.html"


class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy("courseinfo_registration_list_urlpattern")


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
        return render(request,
                      template_name="courseinfo/section_detail.html",
                      context=context)


class SectionList(ListView):
    # the ListView automatically render
    # template_name => <app name>/<model name>_list.html => courseinfo/section_list.html
    # context => model.objects.all()
    model = Section
    # def get(self, request):
    #     return render(
    #         request,
    #         template_name="courseinfo/section_list.html",
    #         context={"section_list": Section.objects.all()}
    #     )


class SectionCreate(CreateView):
    form_class = SectionForm
    model = Section


class SectionUpdate(UpdateView):
    form_class = SectionForm
    model = Section
    template_name = "courseinfo/section_form_update.html"


class SectionDelete(DeleteView):
    model = Section
    success_url = reverse_lazy("courseinfo_section_list_urlpattern")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"section": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/section_refuse_delete.html", context)


class SemesterDetail(View):

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        context = {
            "semester": semester,
        }
        return render(request,
                      template_name="courseinfo/semester_detail.html",
                      context=context)


class SemesterList(ListView):
    model = Semester


class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester


class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = "courseinfo/semester_form_update.html"


class SemesterDelete(DeleteView):
    model = Semester
    success_url = reverse_lazy("courseinfo_semester_list_urlpattern")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"semester": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/semester_refuse_delete.html", context)


class StudentDetail(View):

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        registration_list = student.registrations.all()
        context = {
            "student": student,
            "registration_list": registration_list
        }
        return render(request,
                      template_name="courseinfo/student_detail.html",
                      context=context)


class StudentList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor


class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student


class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = "courseinfo/student_form_update.html"


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy("courseinfo_student_list_urlpattern")

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"student": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/student_refuse_delete.html", context)
