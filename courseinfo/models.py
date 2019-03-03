from django.db import models
from django.urls import reverse


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f"{self.semester_name}"

    def get_absolute_url(self):
        return reverse("courseinfo_semester_detail_urlpattern",
                       kwargs={"pk": self.pk})

    class Meta:
        ordering = ["semester_name"]


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course_number} - {self.course_name}"

    def get_absolute_url(self):
        return reverse("courseinfo_course_detail_urlpattern",
                       kwargs={"pk": self.pk})

    class Meta:
        ordering = ["course_number", "course_name"]
        unique_together = (("course_number", "course_name"),)


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse("courseinfo_instructor_detail_urlpattern",
                       kwargs={"pk": self.pk})

    class Meta:
        ordering = ["last_name", "first_name"]
        unique_together = (("last_name", "first_name"),)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default="")

    def __str__(self):
        if self.nickname == "":
            return f"{self.last_name}, {self.first_name}"
        return f"{self.last_name}, {self.first_name} ({self.nickname})"

    def get_absolute_url(self):
        return reverse("courseinfo_student_detail_urlpattern",
                       kwargs={"pk": self.pk})

    class Meta:
        ordering = ["last_name", "first_name", "nickname"]
        unique_together = (("last_name", "first_name", "nickname"),)


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, related_name="sections", on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name="sections", on_delete=models.PROTECT)
    instructor = models.ForeignKey(Instructor, related_name="sections", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("courseinfo_section_detail_urlpattern",
                       kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.course.course_number} - {self.section_name} ({self.semester.semester_name})"

    class Meta:
        ordering = ["course__course_number", "section_name", "semester__semester_name"]


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, related_name="registrations", on_delete=models.PROTECT)
    section = models.ForeignKey(Section, related_name="registrations", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("courseinfo_registration_detail_urlpattern",
                       kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.section} / {self.student})"

    class Meta:
        ordering = ["section", "student"]
        unique_together = (("section", "student",),)
