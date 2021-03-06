# Generated by Django 2.1.5 on 2019-03-17 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('courseinfo', '0002_auto_20190211_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_number', 'course_name']},
        ),
        migrations.AlterField(
            model_name='registration',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registrations',
                                    to='courseinfo.Section'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registrations',
                                    to='courseinfo.Student'),
        ),
        migrations.AlterField(
            model_name='section',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections',
                                    to='courseinfo.Instructor'),
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections',
                                    to='courseinfo.Semester'),
        ),
        migrations.AlterUniqueTogether(
            name='instructor',
            unique_together={('last_name', 'first_name')},
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('semester', 'course', 'section_name')},
        ),
    ]
