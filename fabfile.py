from __future__ import with_statement
from fabric.api import local, task


@task
def test():
    local('python -m unittest discover')


@task
def coverage():
    local('coverage -x chalk/tests.py')
    local('coverage -rm')
