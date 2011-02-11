#!/bin/bash

devbase=development-deps
venv=$devbase/virtualenv-tw2.jquery
source $venv/bin/activate

pushd $devbase

pushd tw2.devtools
python setup.py install
popd

rm -rf tw2.jquery
hg clone http://bitbucket.org/ralphbean/tw2.jquery
pushd tw2.jquery
python setup.py install_lib install_egg_info
popd

popd

python setup.py install_lib install_egg_info && paster tw2.browser



