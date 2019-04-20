# change setting file

DJANGO_SETTINGS_MODULE=shawn_lee_ez_university.settings.development
DJANGO_SETTINGS_MODULE=shawn_lee_ez_university.settings.production

# migrate

python manage.py showmigrations --settings=shawn_lee_ez_university.settings.production
python manage.py migrate --settings=shawn_lee_ez_university.settings.production

# run server on different settings

python manage.py runserver --settings=shawn_lee_ez_university.settings.development
python manage.py runserver --settings=shawn_lee_ez_university.settings.production

# collect static
python manage.py collectstatic --settings=shawn_lee_ez_university.settings.production

# create super user
python manage.py createsuperuser

# install dependencies
pip install -r shawn_lee_ez_university/requirements/base.txt