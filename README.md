# django-project-template
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
```

Once this is done, it should be a good time to make the repo's initial commit.

