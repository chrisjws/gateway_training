# Copyright 2020 BlueCat Networks. All rights reserved.
import os
import sys
import codecs

from flask import url_for, redirect, render_template, flash, g

from bluecat import route, util
import config.default_config as config
from main_app import app
from .unit_tests_example_form import GenericFormTemplate
from itertools import permutations


def module_path():
    encoding = sys.getfilesystemencoding()
    return os.path.dirname(os.path.abspath(__file__))


# The workflow name must be the first part of any endpoints defined in this file.
# If you break this rule, you will trip up on other people's endpoint names and
# chaos will ensue.
@route(app, '/unit_tests_example/unit_tests_example_endpoint')
@util.workflow_permission_required('unit_tests_example_page')
@util.exception_catcher
@util.ui_secure_endpoint
def unit_tests_example_unit_tests_example_page():
    form = GenericFormTemplate()
    # Remove this line if your workflow does not need to select a configuration
    form.configuration.choices = util.get_configurations(default_val=True)
    return render_template(
        'unit_tests_example_page.html',
        form=form,
        text=util.get_text(module_path(), config.language),
        options=g.user.get_options(),
    )


@route(app, '/unit_tests_example/form', methods=['POST'])
@util.workflow_permission_required('unit_tests_example_page')
@util.exception_catcher
@util.ui_secure_endpoint
def unit_tests_example_unit_tests_example_page_form():
    form = GenericFormTemplate()
    # Remove this line if your workflow does not need to select a configuration
    form.configuration.choices = util.get_configurations(default_val=True)
    if not form.validate_on_submit():
        g.user.logger.info('Form data was not valid.')
        return render_template(
            'unit_tests_example_page.html',
            form=form,
            text=util.get_text(module_path(), config.language),
            options=g.user.get_options(),
        )

    print(form.configuration.data)
    print(form.email.data)
    print(form.password.data)
    print(form.mac_address.data)
    print(form.ip_address.data)
    print(form.url.data)
    print(form.file.data)
    print(form.boolean_checked.data)
    print(form.boolean_unchecked.data)
    print(form.date_time.data)
    print(form.submit.data)

    # Put form processing logic here
    g.user.logger.info('SUCCESS')
    flash('success', 'succeed')
    return redirect(url_for('unit_tests_exampleunit_tests_example_unit_tests_example_page'))


def add_stuff(a, b):
    return a + b


def get_permutations(*args):
    return list(permutations(args))


