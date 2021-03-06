# Generated by Django 2.1.5 on 2019-03-18 00:49

from django.db import migrations, models

YEARS = [
    {"year": 2018},
    {"year": 2019},
    {"year": 2020},
    {"year": 9999},
]


# migration forward procedure
def add_year_data(apps, schema_editor):
    target_model = apps.get_model("courseinfo", "Year")
    for v in YEARS:
        orm_obj = target_model.objects.create(year=v["year"])


# migration backward procedure
def remove_year_data(apps, schema_editor):
    target_model = apps.get_model("courseinfo", "Year")
    for v in YEARS:
        orm_obj = target_model.objects.get(year=v["year"])
        orm_obj.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('courseinfo', '0004_period_schema_and_data_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.RunPython(
            add_year_data,
            remove_year_data
        )
    ]
