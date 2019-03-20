from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

STUDENTS = [
    {
        'first_name': 'Elizabeth',
        'last_name': 'Wilson',
        'nickname': ''
    },
    {
        'first_name': 'Victor',
        'last_name': 'Lewis',
        'nickname': ''
    },
    {
        'first_name': 'Christopher',
        'last_name': 'Paterson',
        'nickname': ''
    },
    {
        'first_name': 'Nicola',
        'last_name': 'Powell',
        'nickname': ''
    },
    {
        'first_name': 'Ava',
        'last_name': 'White',
        'nickname': ''
    },
    {
        'first_name': 'Fiona',
        'last_name': 'Bower',
        'nickname': ''
    },
    {
        'first_name': 'Owen',
        'last_name': 'Reid',
        'nickname': ''
    },
    {
        'first_name': 'Lily',
        'last_name': 'Miller',
        'nickname': ''
    },
    {
        'first_name': 'Deirdre',
        'last_name': 'Gill',
        'nickname': ''
    },
    {
        'first_name': 'Neil',
        'last_name': 'Marshall',
        'nickname': ''
    },
    {
        'first_name': 'Emily',
        'last_name': 'Sanderson',
        'nickname': ''
    },
    {
        'first_name': 'Jessica',
        'last_name': 'King',
        'nickname': ''
    },
    {
        'first_name': 'Adrian',
        'last_name': 'Ogden',
        'nickname': ''
    },
    {
        'first_name': 'Gabrielle',
        'last_name': 'Lee',
        'nickname': ''
    },
    {
        'first_name': 'Joshua',
        'last_name': 'Abraham',
        'nickname': ''
    },
    {
        'first_name': 'Brian',
        'last_name': 'Hill',
        'nickname': ''
    },
    {
        'first_name': 'Bernadette',
        'last_name': 'Buckland',
        'nickname': ''
    },
    {
        'first_name': 'Theresa',
        'last_name': 'Thomson',
        'nickname': ''
    },
    {
        'first_name': 'Ella',
        'last_name': 'Burgess',
        'nickname': ''
    },
    {
        'first_name': 'Donna',
        'last_name': 'James',
        'nickname': ''
    },
    {
        'first_name': 'Audrey',
        'last_name': 'Hudson',
        'nickname': ''
    },
    {
        'first_name': 'Charles',
        'last_name': 'Newman',
        'nickname': ''
    },
    {
        'first_name': 'Adrian',
        'last_name': 'Black',
        'nickname': ''
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Wright',
        'nickname': ''
    },
    {
        'first_name': 'Dorothy',
        'last_name': 'McLean',
        'nickname': ''
    },
    {
        'first_name': 'Stephen',
        'last_name': 'Glover',
        'nickname': ''
    },
    {
        'first_name': 'Gabrielle',
        'last_name': 'Poole',
        'nickname': ''
    },
    {
        'first_name': 'Owen',
        'last_name': 'Edmunds',
        'nickname': ''
    },
    {
        'first_name': 'Amelia',
        'last_name': 'Bower',
        'nickname': ''
    },
    {
        'first_name': 'Ava',
        'last_name': 'Graham',
        'nickname': ''
    },
    {
        'first_name': 'Adam',
        'last_name': 'Taylor',
        'nickname': ''
    },
    {
        'first_name': 'Lily',
        'last_name': 'Ross',
        'nickname': ''
    },
    {
        'first_name': 'Joseph',
        'last_name': 'Skinner',
        'nickname': ''
    },
    {
        'first_name': 'Grace',
        'last_name': 'Greene',
        'nickname': ''
    },
    {
        'first_name': 'Ryan',
        'last_name': 'Parr',
        'nickname': ''
    },
    {
        'first_name': 'Peter',
        'last_name': 'Russell',
        'nickname': ''
    },
    {
        'first_name': 'William',
        'last_name': 'Mills',
        'nickname': ''
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Sharp',
        'nickname': ''
    },
    {
        'first_name': 'Chloe',
        'last_name': 'Anderson',
        'nickname': ''
    },
    {
        'first_name': 'Lisa',
        'last_name': 'Bond',
        'nickname': ''
    },
    {
        'first_name': 'Boris',
        'last_name': 'Paterson',
        'nickname': ''
    },
    {
        'first_name': 'Sam',
        'last_name': 'Wilkins',
        'nickname': ''
    },
    {
        'first_name': 'Max',
        'last_name': 'Lyman',
        'nickname': ''
    },
    {
        'first_name': 'Una',
        'last_name': 'Pullman',
        'nickname': ''
    },
    {
        'first_name': 'Austin',
        'last_name': 'Wilkins',
        'nickname': ''
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Powell',
        'nickname': ''
    },
    {
        'first_name': 'Neil',
        'last_name': 'Grant',
        'nickname': ''
    },
    {
        'first_name': 'Maria',
        'last_name': 'Piper',
        'nickname': ''
    },
    {
        'first_name': 'Andrea',
        'last_name': 'Walsh',
        'nickname': ''
    },
    {
        'first_name': 'Anne',
        'last_name': 'Clark',
        'nickname': ''
    },
    {
        'first_name': 'Tim',
        'last_name': 'Nolan',
        'nickname': ''
    },
    {
        'first_name': 'Victor',
        'last_name': 'Welch',
        'nickname': ''
    },
    {
        'first_name': 'Alan',
        'last_name': 'Davidson',
        'nickname': ''
    },
    {
        'first_name': 'Charles',
        'last_name': 'Churchill',
        'nickname': ''
    },
    {
        'first_name': 'Jessica',
        'last_name': 'Duncan',
        'nickname': ''
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Martin',
        'nickname': ''
    },
    {
        'first_name': 'Maria',
        'last_name': 'Arnold',
        'nickname': ''
    },
    {
        'first_name': 'Sophie',
        'last_name': 'Clark',
        'nickname': ''
    },
    {
        'first_name': 'Jacob',
        'last_name': 'Bailey',
        'nickname': ''
    },
    {
        'first_name': 'Harry',
        'last_name': 'Churchill',
        'nickname': ''
    },
    {
        'first_name': 'Karen',
        'last_name': 'Lyman',
        'nickname': ''
    },
    {
        'first_name': 'Trevor',
        'last_name': 'Hunter',
        'nickname': ''
    },
    {
        'first_name': 'Stephen',
        'last_name': 'Lee',
        'nickname': ''
    },
    {
        'first_name': 'Vanessa',
        'last_name': 'Underwood',
        'nickname': ''
    },
    {
        'first_name': 'Richard',
        'last_name': 'Kelly',
        'nickname': ''
    },
    {
        'first_name': 'Amelia',
        'last_name': 'Campbell',
        'nickname': ''
    },
    {
        'first_name': 'Zoe',
        'last_name': 'McLean',
        'nickname': ''
    },
    {
        'first_name': 'Sam',
        'last_name': 'Forsyth',
        'nickname': ''
    },
    {
        'first_name': 'Phil',
        'last_name': 'Wright',
        'nickname': ''
    },
    {
        'first_name': 'Maria',
        'last_name': 'Hudson',
        'nickname': ''
    },
    {
        'first_name': 'Diana',
        'last_name': 'Mackay',
        'nickname': ''
    },
    {
        'first_name': 'Stewart',
        'last_name': 'Ellison',
        'nickname': ''
    },
    {
        'first_name': 'Sue',
        'last_name': 'Edmunds',
        'nickname': ''
    },
    {
        'first_name': 'Karen',
        'last_name': 'Ogden',
        'nickname': ''
    },
    {
        'first_name': 'Carol',
        'last_name': 'Martin',
        'nickname': ''
    },
    {
        'first_name': 'Oliver',
        'last_name': 'Wilkins',
        'nickname': ''
    },
    {
        'first_name': 'Adam',
        'last_name': 'Bower',
        'nickname': ''
    },
    {
        'first_name': 'Katherine',
        'last_name': 'Clarkson',
        'nickname': ''
    },
    {
        'first_name': 'Carol',
        'last_name': 'Turner',
        'nickname': ''
    },
    {
        'first_name': 'Ian',
        'last_name': 'James',
        'nickname': ''
    },
    {
        'first_name': 'Una',
        'last_name': 'McLean',
        'nickname': ''
    },
    {
        'first_name': 'Heather',
        'last_name': 'Clark',
        'nickname': ''
    },
    {
        'first_name': 'Liam',
        'last_name': 'Ellison',
        'nickname': ''
    },
    {
        'first_name': 'Madeleine',
        'last_name': 'Gill',
        'nickname': ''
    },
    {
        'first_name': 'Warren',
        'last_name': 'Berry',
        'nickname': ''
    },
    {
        'first_name': 'Yvonne',
        'last_name': 'Lyman',
        'nickname': ''
    },
    {
        'first_name': 'Claire',
        'last_name': 'Abraham',
        'nickname': ''
    },
    {
        'first_name': 'Andrea',
        'last_name': 'Hemmings',
        'nickname': ''
    },
    {
        'first_name': 'Claire',
        'last_name': 'Clarkson',
        'nickname': ''
    },
    {
        'first_name': 'Max',
        'last_name': 'Mackenzie',
        'nickname': ''
    },
    {
        'first_name': 'Luke',
        'last_name': 'Ince',
        'nickname': ''
    },
    {
        'first_name': 'Samantha',
        'last_name': 'Tucker',
        'nickname': ''
    },
    {
        'first_name': 'James',
        'last_name': 'Lewis',
        'nickname': ''
    },
    {
        'first_name': 'Wendy',
        'last_name': 'Cornish',
        'nickname': ''
    },
    {
        'first_name': 'Evan',
        'last_name': 'Hamilton',
        'nickname': ''
    },
    {
        'first_name': 'Caroline',
        'last_name': 'Lee',
        'nickname': ''
    },
    {
        'first_name': 'Stephanie',
        'last_name': 'Smith',
        'nickname': ''
    },
    {
        'first_name': 'Lily',
        'last_name': 'Jones',
        'nickname': ''
    },
    {
        'first_name': 'Melanie',
        'last_name': 'Peake',
        'nickname': ''
    },
    {
        'first_name': 'Richard',
        'last_name': 'Smith',
        'nickname': ''
    },
    {
        'first_name': 'Neil',
        'last_name': 'Randall',
        'nickname': ''
    },
    {
        'first_name': 'John',
        'last_name': 'Quinn',
        'nickname': ''
    },
    {
        'first_name': 'Emma',
        'last_name': 'Bell',
        'nickname': ''
    },
    {
        'first_name': 'Stephanie',
        'last_name': 'Forsyth',
        'nickname': ''
    },
    {
        'first_name': 'Claire',
        'last_name': 'Young',
        'nickname': ''
    },
    {
        'first_name': 'Felicity',
        'last_name': 'Avery',
        'nickname': ''
    },
    {
        'first_name': 'Robert',
        'last_name': 'Glover',
        'nickname': ''
    },
    {
        'first_name': 'Paul',
        'last_name': 'Tucker',
        'nickname': ''
    },
    {
        'first_name': 'Abigail',
        'last_name': 'Morrison',
        'nickname': ''
    },
    {
        'first_name': 'Carl',
        'last_name': 'Ross',
        'nickname': ''
    },
    {
        'first_name': 'Jack',
        'last_name': 'Parr',
        'nickname': ''
    },
    {
        'first_name': 'Owen',
        'last_name': 'Ogden',
        'nickname': ''
    },
    {
        'first_name': 'Grace',
        'last_name': 'Ball',
        'nickname': ''
    },
    {
        'first_name': 'Felicity',
        'last_name': 'Hill',
        'nickname': ''
    },
    {
        'first_name': 'Dylan',
        'last_name': 'Fisher',
        'nickname': ''
    },
    {
        'first_name': 'Angela',
        'last_name': 'Black',
        'nickname': ''
    },
    {
        'first_name': 'Carolyn',
        'last_name': 'Murray',
        'nickname': ''
    },
    {
        'first_name': 'Michelle',
        'last_name': 'Morrison',
        'nickname': ''
    },
    {
        'first_name': 'Penelope',
        'last_name': 'Glover',
        'nickname': ''
    },
    {
        'first_name': 'Frank',
        'last_name': 'Newman',
        'nickname': ''
    },
    {
        'first_name': 'Penelope',
        'last_name': 'Blake',
        'nickname': ''
    },
    {
        'first_name': 'Theresa',
        'last_name': 'Russell',
        'nickname': ''
    },
    {
        'first_name': 'Trevor',
        'last_name': 'Cameron',
        'nickname': ''
    },
    {
        'first_name': 'Stephen',
        'last_name': 'Cornish',
        'nickname': ''
    },
    {
        'first_name': 'Anthony',
        'last_name': 'Parr',
        'nickname': ''
    },

]


def add_student_data(apps, schema_editor):
    student_class = apps.get_model('courseinfo', 'Student')
    for student in STUDENTS:
        try:
            duplicate_object = student_class.objects.get(
                first_name=student['first_name'],
                last_name=student['last_name'],
                nickname=student['nickname']
            )
            print('Duplicate student entry not added to students table:', student['first_name'], student['last_name'],
                  student['nickname'])
        except ObjectDoesNotExist:
            student_object = student_class.objects.create(
                first_name=student['first_name'],
                last_name=student['last_name'],
                nickname=student['nickname']
            )


def remove_student_data(apps, schema_editor):
    student_class = apps.get_model('courseinfo', 'Student')
    for student in STUDENTS:
        student_object = student_class.objects.get(
            first_name=student['first_name'],
            last_name=student['last_name'],
            nickname=student['nickname']
        )
        student_object.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('courseinfo', '0008_load_instructor_test_data'),
    ]

    operations = [
        migrations.RunPython(
            add_student_data,
            remove_student_data
        )
    ]
