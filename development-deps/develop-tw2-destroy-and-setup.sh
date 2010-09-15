#!/bin/bash -e

devbase=development-deps
venv=$devbase/virtualenv-tw2.jquery.ui
$(
    rm -rf $venv
) || echo "Did not destroy $venv"

virtualenv $venv --no-site-packages

source $venv/bin/activate

pushd $devbase

hg clone http://bitbucket.org/paj/tw2core || echo "tw2core exists."
hg clone http://bitbucket.org/paj/tw2devtools || echo "tw2devtools exists."
hg clone http://bitbucket.org/paj/tw2forms || echo "tw2devtools exists."
git clone git://github.com/ralphbean/tw2.jquery.core.git || echo "tw2.jquery.core exists."

pip install genshi
pip install formencode

pushd tw2core ;  python setup.py develop ; popd
pushd tw2forms ; python setup.py develop ; popd
pushd tw2devtools ; python setup.py develop ; popd
pushd tw2.jquery.core ; python setup.py develop ; popd

pushd # $devbase
