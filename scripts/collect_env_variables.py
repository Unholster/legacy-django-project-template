"""
This script reads all environment variables referenced in settings, dev_settings and prod_settings.
python script/collect_env_variables.py > .env will create an empty .env file.
"""
import os
import sys

from milieu import M


def monkeypatch_milieu():
    attrs = set()
    old_get_attr = M.__getattr__

    def monkey_patched(self, key):
        attrs.add(key)
        return old_get_attr(self, key)

    M.__getattr__ = monkey_patched
    return attrs


attrs = monkeypatch_milieu()
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
exec('from {{project_name}}.conf.settings import *')
exec('from {{project_name}}.conf.dev_settings import *')
exec('from {{project_name}}.conf.prod_settings import *')
attrs = sorted(attrs)
print('\n'.join(attrs))
