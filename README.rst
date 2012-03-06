tw2.jqplugins.ui
=====================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery UI: http://jqueryui.com/
.. _jQuery: http://jquery.com/

tw2.jqplugins.ui is a `toscawidgets2 (tw2)`_ wrapper for `jQuery UI`_.

Live Demo
---------
Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.ui>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.ui>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.ui>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.ui/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`jQuery`_ is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax interactions
for rapid web development. jQuery is designed to change the way that
you write JavaScript.

`jQuery UI`_ provides abstractions for low-level interaction and animation,
advanced effects and high-level, themeable widgets, built on top of the
jQuery JavaScript Library, that you can use to build highly interactive
web applications.

This module, tw2.jqplugins.ui, provides `toscawidgets2 (tw2)`_ access to
`jQuery UI`_ widgets.

Sampling tw2.jqplugins.ui in the WidgetBrowser
----------------------------------------------

The best way to scope out ``tw2.jqplugins.ui`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.ui/tw2/jqplugins/ui/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.ui.git
    $ cd tw2.jqplugins.ui
    $ mkvirtualenv tw2.jqplugins.ui
    (tw2.jqplugins.ui) $ pip install tw2.devtools
    (tw2.jqplugins.ui) $ python setup.py develop
    (tw2.jqplugins.ui) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
