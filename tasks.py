from invoke import task, run

import os
import sys
import shutil

@task
def clean():
    """Remove generated files"""
    shutil.rmtree('static/font')
    os.remove('static/css/materialize.min.css')

@task
def build():
    """Build local version of site"""
    run('sassc -t compressed materialize-src/sass/materialize.scss static/css/materialize.min.css')

    run('rsync -a --delete materialize-src/font/ static/font')

    shutil.copy2('jquery-2.1.4.min.js', 'static/js/jquery.min.js')
    shutil.copy2('materialize-src/js/bin/materialize.min.js', 'static/js/')