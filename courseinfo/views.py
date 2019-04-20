from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from courseinfo.forms import CourseForm, InstructorForm, SectionForm, SemesterForm, StudentForm, RegistrationForm
from .models import Instructor, Section, Course, Semester, Student, Registration
from .utils import PageLinksMixin


class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "courseinfo.view_course"

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


class CourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course
    permission_required = "courseinfo.view_course"


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CourseForm
    model = Course
    permission_required = "courseinfo.add_course"


class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CourseForm
    model = Course
    template_name = "courseinfo/course_form_update.html"
    permission_required = "courseinfo.edit_course"


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy("courseinfo_course_list_urlpattern")
    permission_required = "courseinfo.delete_course"

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"course": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/course_refuse_delete.html", context)


class InstructorDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "courseinfo.view_instructor"

    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        context = {
            "instructor": instructor,
            "section_list": instructor.sections.all(),
        }
        return render(request,
                      template_name="courseinfo/instructor_detail.html",
                      context=context)


class InstructorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor
    permission_required = "courseinfo.view_instructor"


class InstructorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = InstructorForm
    model = Instructor
    permission_required = "courseinfo.add_instructor"


class InstructorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = "courseinfo/instructor_form_update.html"
    permission_required = "courseinfo.change_instructor"


class InstructorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Instructor
    success_url = reverse_lazy("courseinfo_instructor_list_urlpattern")
    permission_required = "courseinfo.delete_instructor"

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"instructor": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/instructor_refuse_delete.html", context)


class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "courseinfo.view_registration"

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


class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Registration
    permission_required = "courseinfo.view_registration"


class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RegistrationForm
    model = Registration
    permission_required = "courseinfo.add_registration"


class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = "courseinfo/registration_form_update.html"
    permission_required = "courseinfo.change_registration"


class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registration
    success_url = reverse_lazy("courseinfo_registration_list_urlpattern")
    permission_required = "courseinfo.delete_registration"


class SectionDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "courseinfo.view_section"

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


class SectionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    # the ListView automatically render
    # template_name => <app name>/<model name>_list.html => courseinfo/section_list.html
    # context => model.objects.all()
    permission_required = "courseinfo.view_section"
    model = Section


class SectionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SectionForm
    model = Section
    permission_required = "courseinfo.add_section"


class SectionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SectionForm
    model = Section
    template_name = "courseinfo/section_form_update.html"
    permission_required = "courseinfo.update_section"


class SectionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Section
    success_url = reverse_lazy("courseinfo_section_list_urlpattern")
    permission_required = "courseinfo.delete_section"

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"section": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/section_refuse_delete.html", context)


class SemesterDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "courseinfo.view_semester"

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        context = {
            "semester": semester,
        }
        return render(request,
                      template_name="courseinfo/semester_detail.html",
                      context=context)


class SemesterList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Semester
    permission_required = "courseinfo.view_semester"


class SemesterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SemesterForm
    model = Semester
    permission_required = "courseinfo.add_semester"


class SemesterUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = "courseinfo/semester_form_update.html"
    permission_required = "courseinfo.change_semester"


class SemesterDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Semester
    success_url = reverse_lazy("courseinfo_semester_list_urlpattern")
    permission_required = "courseinfo.delete_semester"

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"semester": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/semester_refuse_delete.html", context)


class StudentDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "courseinfo.view_student"

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


class StudentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor
    permission_required = "courseinfo.view_student"


class StudentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StudentForm
    model = Student
    permission_required = "courseinfo.add_student"


class StudentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = StudentForm
    model = Student
    template_name = "courseinfo/student_form_update.html"
    permission_required = "courseinfo.change_student"


class StudentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("courseinfo_student_list_urlpattern")
    permission_required = "courseinfo.delete_student"

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            context = {"student": get_object_or_404(self.model, pk=kwargs["pk"])}
            return render(request, "courseinfo/student_refuse_delete.html", context)
