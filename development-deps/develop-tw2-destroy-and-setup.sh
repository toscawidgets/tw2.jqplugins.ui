#!/bin/bash -e

devbase=development-deps
venv=$devbase/virtualenv-tw2.jquery
$(
    rm -rf $venv
) || echo "Did not destroy $venv"

virtualenv $venv --no-site-packages

source $venv/bin/activate

pushd $devbase

pip install genshi
pip install mako
pip install formencode

hg clone http://bitbucket.org/paj/tw2core || \
        (pushd tw2core && hg pull && hg update && popd)
hg clone http://bitbucket.org/ralphbean/tw2.devtools || \
        (pushd tw2.devtools && hg pull && hg update && popd)
hg clone http://bitbucket.org/paj/tw2forms || \
        (pushd tw2forms && hg pull && hg update && popd)
hg clone http://bitbucket.org/ralphbean/tw2.jquery || \
        (pushd tw2.jquery && hg pull && hg update && popd)
#hg clone https://ralphbean@bitbucket.org/toscawidgets/tw2jquery || \
#        (pushd tw2jquery && hg pull && hg update && popd)

pushd tw2core ;  python setup.py install ; popd
pushd tw2forms ; python setup.py install ; popd
pushd tw2.devtools ; python setup.py install ; popd
pushd tw2.jquery ; python setup.py install_lib install_egg_info ; popd

popd # $devbase
