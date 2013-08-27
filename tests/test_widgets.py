from tw2.core.testbase import WidgetTest

import tw2.jqplugins.ui.widgets as w
import tw2.jqplugins.ui.samples as s


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
$(document).ready(function() {
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
    <input name="foo" id="foo" type="text">
<script type="text/javascript">
$(document).ready(function() {
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
     <input name="foo" id="foo" value="foobar" type="text">
<script type="text/javascript">
$(document).ready(function() {
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
$(document).ready(function() {
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
<input name="foo" type="text" id="foo">
<script type="text/javascript">
$(document).ready(function() {
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
$(document).ready(function() {
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
$(document).ready(function() {
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
$(document).ready(function() {
    $("#foo").slider({});
});
</script>
</div>
"""


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
$(document).ready(function() {
    $("#foo").tabs({});
});
</script>
</div>
"""


class TestEmptyTabsWidget(WidgetTest):
    widget = w.TabsWidget
    attrs = {'id' : 'foo'}
    params = {'items':[]}
    expected = """
<div id="foo:wrapper">
<div id="foo">
    <ul>
    </ul>
</div>
<script type="text/javascript">
$(document).ready(function() {
    $("#foo").tabs({});
});
</script>
</div>
"""


class TestDemoButtonSetCheckbox(WidgetTest):
    widget = s.DemoButtonSetCheckbox
    attrs = {'id':'foo'}
    params = {}
    expected = """
<div id="foo:wrapper">
    <div id="foo">
            <input type="checkbox" id="cb_1"/>
        <label for="cb_1">BBC1</label>
            <input type="checkbox" id="cb_2" checked="checked" />
        <label for="cb_2">BBC2</label>
            <input type="checkbox" id="cb_3"/>
        <label for="cb_3">BBC3</label>
            <input type="checkbox" id="cb_4"/>
        <label for="cb_4">BBC4</label>
    </div>
    <script type="text/javascript">
        $(document).ready(function() {
            $("#foo").buttonset({});
                $("#foo input").click(
        function(e) {
            var areChecked = {};
            var button_ids = new Array('cb_1', 'cb_2', 'cb_3', 'cb_4');
            for ( i in button_ids ) {
                areChecked[button_ids[i]] =  $('#'+button_ids[i]).attr('checked');
            }
            alert( $(this).attr('id') + ' : was clicked \\n\\n' +
                   'contents of variable "areChecked": \\n' +
                   'cb_1: ' + areChecked['cb_1'] + '\\n' +
                   'cb_2: ' + areChecked['cb_2'] + '\\n' +
                   'cb_3: ' + areChecked['cb_3'] + '\\n' +
                   'cb_4: ' + areChecked['cb_4']
                   )
        }
        );
        });
    </script>
</div>
"""


class TestDemoButtonSetRadio(WidgetTest):
    widget = s.DemoButtonSetRadio
    attrs = {'id':'foo'}
    params = {}
    expected = """
<div id="foo:wrapper">
    <div id="foo">
            <input name="foo" type="radio" id="rb_1"/>
        <label for="rb_1">BBC1</label>
            <input name="foo" type="radio" id="rb_2" checked="checked" />
        <label for="rb_2">BBC2</label>
            <input name="foo" type="radio" id="rb_3"/>
        <label for="rb_3">BBC3</label>
    </div>
    <script type="text/javascript">
        $(document).ready(function() {
            $("#foo").buttonset({});
                $("#foo input").click(function(e) {alert($(this).attr('id') + ' : was selected');});
        });
    </script>
</div>"""
