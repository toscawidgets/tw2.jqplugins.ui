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

import tw2.jquery_ui.widgets as w

# No tests for core for now
class TestAccordionWidget(WidgetTest):
    widget = w.AccordionWidget
    attrs = {'id' : 'foo'}
    params = {'items' : [('foo1', 'foo1c'), ('foo2', 'foo2c')]}
    expected = """<div id="foo-wrapper">
<div id="foo">
        <h3><a href="#">foo1</a></h3>
        <div>foo1c</div>
        <h3><a href="#">foo2</a></h3>
        <div>foo2c</div>
</div>
<script type="text/javascript">
$(function() {
    $("#foo").accordion({});
});
</script>
</div>"""


