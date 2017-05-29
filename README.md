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
pip install Django

# Start project using template, in the repo's root
# The --extension=ini parameter is important so that the pytest.ini file included is created correctly
django-admin startproject --template=https://github.com/Unholster/django-project-template/archive/channels.zip --extension=ini project_name .

# Install the project in the virtualenv
# Requirements first
# Finally the project itself as an editable package
pip install -r requirements.txt
pip install -e .
```
To set up tests, replace `project_name` in your `py.test` file with your project name


Once this is done, it should be a good time to make the repo's initial commit.

## Basic configuration
Most of the Django settings are delegated to environment variables. The basic ones you need to set before the project will work are:
For development, you can store an .env file at the root of the project that will be automatically loaded. The .env file should be in your .gitignore.

### SECRET_KEY
Set this to anything you want in development (i.e. `export SECRET_KEY=foo`. When moving to production, the production's environment variable should have a strong secret key.

### DATABASE_URL
Set this to the URL for your database. We typically use Postgres and, in development, name the database as the project requiring no credentials for local access. Therefore our development database urls typically look like this: `postgres://localhost/project_name`
Once you have your database setup remember to run `manage.py migrate`

### DJANGO_ENV
Our project layout includes 4 settings files under the `project_name/conf` directory:
* `settings.py`: The main settings file. All basic settings should be defined here
* `dev_settings.py`: Default env. This file first includes the main settings file, then applies any overrides specific to development environments. The dev_settings loads the env.
* `test_settings.py`: This file first includes the main settings file, then applies any overrides specific to test environments (i.e. used when running automated tests). The pytest.ini included in the template, includes a directive to automatically switch to this settings file when running tests.
* `prod_settings.py`: This file first includes the main settings file, then applies any overrides specific to production environments (i.e. used when running automated tests).
In order to switch between these files you may use the `DJANGO_ENV` environment variable, setting it to `dev`, `prod` or `test`. The `manage.py` will know how to switch between settings files based on this variable.

### SENTRY_DSN
Set up the DSN of your [sentry](sentry.io) project, this will only work when the server is run on development mode, you can test your sentry configuration with
```
export DJANGO_ENV=prod
export SECRET_KEY=123124124
export DJANGO_ENV=prod
export RAVEN_DSN=YOUR SENTRY DSN
./manage.py raven test
```


### PAPERTRAIL_URL, PAPERTRAIL_PORT
The papertrail configuration for your project.
You can test papertrail as following
```
export DJANGO_ENV=prod
export PAPERTRAIL_URL=logs5.papertrailapp.com
export PAPERTRAIL_PORT=11490
export SECRET_KEY=123124124
./manage.py shell -c "import logging; l=logging.getLogger('test'); l.info('testing papertrail')"
```


## Managing staticfile compilation
**Important** : Please consider developing an Single Page Application for
heavily customized front end work. We try to avoid maintain

Files stored under `project_name/static` will be served and handled as staticfiles.
In addition, the project is installed from this template with a simple pipeline for compiled assets (Coffeescript, SASS).
These should be stored under `project_name/static-src/{coffee,sass}` and will be compiled into `project_name\{compiled-js,compiled-css}`.
In order to compile these assets you can use the bundled command: `manage.py grunt`. This will run a grunt watcher that compiels the sources whenever they are modified.

For the pipeline to work, there is a little bit of setup required after creating the project:
```
cd project_name/grunt
npm install
```

Once this is completed you can run the watcher with `manage.py grunt`. The directory you run the command from is irrelevant.
