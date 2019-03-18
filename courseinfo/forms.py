from django import forms

from courseinfo.models import Course, Instructor, Registration, Semester, Student, Section


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"

        def clean_first_name(self):
            return self.cleaned_data["first_name"].strip()

        def clean_last_name(self):
            return self.cleaned_data["last_name"].strip()


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
