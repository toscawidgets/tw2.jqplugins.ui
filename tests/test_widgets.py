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

import tw2.jqplugins.ui.widgets as w

class TestAccordionWidget(WidgetTest):
    widget = w.AccordionWidget
    attrs = {'id' : 'foo'}
    params = {'items' : [('foo1', 'foo1c'), ('foo2', 'foo2c')]}
    expected = """
<div id="foo:wrapper">
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
</div>
"""

class TestAutocompleteWidget(WidgetTest):
    widget = w.AutocompleteWidget
    attrs = {'id' : 'foo'}
    params = {}
    expected = """
<div id="foo:wrapper">
<input id="foo" value="" />
<script type="text/javascript">
$(function() {
    $("#foo").autocomplete({});
});
</script>
</div>
"""

class TestCategoryAutocompleteWidget(WidgetTest):
    widget = w.CategoryAutocompleteWidget
    attrs = {'id' : 'foo'}
    params = {'value' : 'foobar'}
    expected = """
<div id="foo:wrapper">
    <style>
    .ui-autocomplete-category {
        font-weight: bold;
        padding: .6em .12em;
        margin: .8em 0 .2em;
        line-height: 1.5;
    }
    </style>
     <input id="foo" value="foobar">
<script type="text/javascript">
$(function() {
    $("#foo").catcomplete({});
});
</script>
<div>
<style type="text/css">
    .tw2-jquery-faded {color:#AAA;}
    .tw2-jquery-focused {color:#000;}
</style>
<script type="text/javascript">
$(document).ready( function () {
    var selector = "#foo";
    $(selector).focus( function () {
        if ( $(selector).val()=="foobar" ) {
            $(selector).val("");
        }
        $(selector).addClass("tw2-jquery-focused");
        $(selector).removeClass("tw2-jquery-faded");
    });
    $(selector).blur( function () {
        if ( $(selector).val()=="" ) {
            $(selector).val( "foobar" );
            $(selector).addClass("tw2-jquery-faded");
            $(selector).removeClass("tw2-jquery-focused");
        }
    });
    $(selector).addClass("tw2-jquery-faded");
});
</script>
</div>
</div>"""

class TestButtonWidget(WidgetTest):
    widget = w.ButtonWidget
    attrs = {'id' : 'foo'}
    params = {}
    expected = """
<div id="foo:wrapper">
<button id="foo"></button>
<script type="text/javascript">
$(function() {
    $("#foo").button({});
});
</script>
</div>
"""

class TestDatePickerWidget(WidgetTest):
    widget = w.DatePickerWidget
    attrs = {'id' : 'foo'}
    params = {}
    expected = """
<div id="foo:wrapper">
<input type="text" id="foo">
<script type="text/javascript">
$(function() {
    $("#foo").datepicker({});
});
</script>
</div>
"""

class TestDialogWidget(WidgetTest):
    widget = w.DialogWidget
    attrs = {'id' : 'foo'}
    params = {'value' : 'biz'}
    expected = """
<div id="foo:wrapper">
<div id="foo"> biz </div>
<script type="text/javascript">
$(function() {
    $("#foo").dialog({});
});
</script>
</div>
"""

class TestProgressBarWidget(WidgetTest):
    widget = w.ProgressBarWidget
    attrs = {'id' : 'foo'}
    params = {'options' : {'value' : 28}}
    expected = """
<div id="foo:wrapper">
<div id="foo"></div>
<script type="text/javascript">
$(function() {
    $("#foo").progressbar({"value": 28});
});
</script>
</div>
"""

class TestSliderWidget(WidgetTest):
    widget = w.SliderWidget
    attrs = {'id' : 'foo'}
    params = {}
    expected = """
<div id="foo:wrapper">
<div id="foo"></div>
<script type="text/javascript">
$(function() {
    $("#foo").slider({});
});
</script>
</div>
"""

# Why does this test fail?  I dunno.  Halp!!!
class TestTabsWidget(WidgetTest):
    widget = w.TabsWidget
    attrs = {'id' : 'foo'}
    params = {'items':[('foo1', 'foo2')]}
    expected = """
<div id="foo:wrapper">
<div id="foo">
    <ul>
        <li><a href="#foo:0">
            foo1
        </a></li>
    </ul>
    <div id="foo:0">
        foo2
    </div>
</div>
<script type="text/javascript">
$(function() {
    $("#foo").tabs({});
});
</script>
</div>
"""
