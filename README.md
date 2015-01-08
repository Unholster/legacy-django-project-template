# Unholster's Django project template
Project template for Django

## Starting a project using this template
We typically create the project inside an already existing repository and use `virtualenwrapper` to manage a virtualenv under which development is performed.

repo-name: Is the name of the repository
project_name: Is the name of the Django project. Does not need to be the same as the repo name, and in our case usually isn't.

```
# Init repo
git init repo-name
cd repo-name

# Create virtualenv
mkvirtualenv project_name

# Install Django
pip insall django

# Start project using template, in the repo's root
# The --extension=ini parameter is important so that the pytest.ini file included is created correctly
django-admin startproject --template=https://github.com/Unholster/django-project-template/archive/master.zip --extension=ini project_name .

# Install the project in the virtualenv
# Requirements first
# Finally the project itself as an editable package
pip install -r requirements.txt
pip install -e .
```

Once this is done, it should be a good time to make the repo's initial commit.

## Basic configuration
Most of the Django settings are delegated to environment variables. The basic ones you need to set before the project will work are:

### SECRET_KEY
Set this to anything you want in development (i.e. `export SECRET_KEY=foo`. When moving to production, the production's environment varialbe should have a strong secret key.

### DATABASE_URL
Set this to the URL for your database. We typically use Postgres and, in development, name the database as the project requiring no credentials for local access. Therefore our development database urls typically look like this: `postgres://localhost/project_name`
Once you have your database setup remember to run `manage.py migrate`

### DJANGO_ENV
Our project layout includes 4 settings files under the `project_name/conf` directory:
* `settings.py`: The main settings file. All basic settings should be defined here
* `dev_settings.py`: This file first includes the main settings file, then applies any overrides specific to development environments.
* `test_settings.py`: This file first includes the main settings file, then applies any overrides specific to test environments (i.e. used when running automated tests). The pytest.ini included in the template, includes a directive to automatically switch to this settings file when running tests.
* `prod_settings.py`: This file first includes the main settings file, then applies any overrides specific to production environments (i.e. used when running automated tests).

In order to switch between these files you may use the `DJANGO_ENV` environment variable, setting it to `dev`, `prod` or `test`. The `manage.py` will know how to switch between settings files based on this variable.
