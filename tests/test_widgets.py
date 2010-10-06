from tw2.jquery_core.widgets import JQueryWidget
from webob import Request
from webob.multidict import NestedMultiDict
from tw2.core.testbase import assert_in_xml, assert_eq_xml, WidgetTest
from nose.tools import raises
from cStringIO import StringIO
from tw2.core import EmptyField, IntValidator, ValidationError
from cgi import FieldStorage
import formencode

import webob
if hasattr(webob, 'NestedMultiDict'):
    from webob import NestedMultiDict
else:
    from webob.multidict import NestedMultiDict

import tw2.jquery_core.base as base
import tw2.jquery_core.widgets as widgets

# No tests for core for now
