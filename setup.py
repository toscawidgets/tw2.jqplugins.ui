from setuptools import setup, find_packages

# Hack to get tests working on python 2.7
import multiprocessing
import logging

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

# Requirements to install buffet plugins and engines
_extra_genshi = ["Genshi >= 0.3.5"]
_extra_mako = ["Mako >= 0.1.1"]


setup(
    name='tw2.jqplugins.ui',
    version='2.0.1',
    description='toscawidgets2 wrapper for jquery-ui',
    long_description=long_description,
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    license='MIT',
    url='http://github.com/toscawidgets/tw2.jqplugins.ui',
    install_requires=[
        "tw2.core>=2.0b5",
        "tw2.forms",
        "tw2.jquery",
        ],
    extras_require = {
        'genshi': _extra_genshi,
        'mako': _extra_mako,
    },
    tests_require = [
        'nose',
        'FormEncode',
        'WebTest',
        'sieve',
    ] + _extra_genshi + _extra_mako,
    packages=['tw2', 'tw2.jqplugins', 'tw2.jqplugins.ui'],
    namespace_packages=['tw2', 'tw2.jqplugins'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jqplugins.ui
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'License :: OSI Approved :: MIT License',
    ],
)
