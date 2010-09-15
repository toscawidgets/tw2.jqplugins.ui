#!/bin/bash

devbase=development-deps
venv=$devbase/virtualenv-tw2.jquery.ui
source $venv/bin/activate

python setup.py develop && paster tw2.browser



