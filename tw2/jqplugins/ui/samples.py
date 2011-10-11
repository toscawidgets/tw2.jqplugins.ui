"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from widgets import (
    AccordionWidget,
    AutocompleteWidget,
    CategoryAutocompleteWidget,
    ButtonWidget,
    DatePickerWidget,
    DialogWidget,
    ProgressBarWidget,
    SliderWidget,
    TabsWidget,
    ButtonSetRadio,
    ButtonSetCheckbox,
)


some_items = [
        ('Section 1',
         """
                <p>
                Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam. Integer
                ut neque. Vivamus nisi metus, molestie vel, gravida in, condimentum sit
                amet, nunc. Nam a nibh. Donec suscipit eros. Nam mi. Proin viverra leo ut
                odio. Curabitur malesuada. Vestibulum a velit eu ante scelerisque vulputate.
                </p>
         """),
        ('Section 2',
         """
                <p>
                Sed non urna. Donec et ante. Phasellus eu ligula. Vestibulum sit amet
                purus. Vivamus hendrerit, dolor at aliquet laoreet, mauris turpis porttitor
                velit, faucibus interdum tellus libero ac justo. Vivamus non quam. In
                suscipit faucibus urna.
                </p>
        """),
        ('Section 3',
         """
                <p>
                Nam enim risus, molestie et, porta ac, aliquam ac, risus. Quisque lobortis.
                Phasellus pellentesque purus in massa. Aenean in pede. Phasellus ac libero
                ac tellus pellentesque semper. Sed ac felis. Sed commodo, magna quis
                lacinia ornare, quam ante aliquam nisi, eu iaculis leo purus venenatis dui.
                </p>
                <ul>
                    <li>List item one</li>
                    <li>List item two</li>
                    <li>List item three</li>
                </ul>
         """),
        ('Section 4',
         """
                <p>
                Cras dictum. Pellentesque habitant morbi tristique senectus et netus
                et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in
                faucibus orci luctus et ultrices posuere cubilia Curae; Aenean lacinia
                mauris vel est.
                </p>
                <p>
                Suspendisse eu nisl. Nullam ut libero. Integer dignissim consequat lectus.
                Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
                inceptos himenaeos.
                </p>
         """),
    ]
class DemoAccordionWidget(AccordionWidget):
    items = some_items
    options = {
        'fillSpace' : True,
        'active' : 2
    }

class DemoAutocompleteWidget(AutocompleteWidget):
    options = {
        'source' : [
            "ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++",
            "Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran", "Groovy",
            "Haskell", "Java", "JavaScript", "Lisp", "Perl", "PHP", "Python",
            "Ruby", "Scala", "Scheme"
        ],
    }
class DemoCategoryAutocompleteWidget(CategoryAutocompleteWidget):
    value = "Try 'n' or 'a'"
    options = {
        'source' : [
            { 'label': "anders", 'category': "" },
            { 'label': "andreas", 'category': "" },
            { 'label': "antal", 'category': "" },
            { 'label': "annhhx10", 'category': "Products" },
            { 'label': "annk K12", 'category': "Products" },
            { 'label': "annttop C13", 'category': "Products" },
            { 'label': "anders andersson", 'category': "People" },
            { 'label': "andreas andersson", 'category': "People" },
            { 'label': "andreas johnson", 'category': "People" }
        ]
    }
    
class DemoButtonWidget(ButtonWidget):
    type = 'button'
    events = {
        'click': "function() { alert( 'Hello world!' ) }"
    }
    options = {
        'label' : "This is a jQuery UI button",
    }

class DemoButtonSetRadio(ButtonSetRadio):
    items = [
        {'id':'rb_1', 'label':'BBC1'},
        {'id':'rb_2', 'label':'BBC2'},
        {'id':'rb_3', 'label':'BBC3'},
    ]
    checked_item = 'rb_2'
    # demonstrates acquisition of the selected radio button
    events = {
        'click': "function(e) {alert($(this).attr('id') + ' : was selected');}"
    }

class DemoButtonSetCheckbox(ButtonSetCheckbox):
    items = [
        {'id':'cb_1', 'label':'BBC1'},
        {'id':'cb_2', 'label':'BBC2', 'isSelected':True},
        {'id':'cb_3', 'label':'BBC3'},
        {'id':'cb_4', 'label':'BBC4'},
    ]
    # demonstrates acquisition of checkbutton settings [checked/unchecked]
    btn_ids = [i['id'] for i in items]
    events = {
        "click": '''
        function(e) {
            var areChecked = {};
            var button_ids = new Array(%s);
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
        ''' % (str(btn_ids)[1:-1])
    }

class DemoDatePickerWidget(DatePickerWidget):
    pass

class DemoDialogWidget(DialogWidget):
    options = {
        'title' : 'Basic Dialog',
    }
    value = """
    <p>
    This is the default dialog which is useful for displaying information.
    The dialog window can be moved, resized and closed with the 'x' icon.
    </p>

    <p>It is likely displayed at the top of the page ;p</p>
    """

class DemoProgressBarWidget(ProgressBarWidget):
    options = {
        'value' : 28
    }

class DemoSliderWidget(SliderWidget):
    pass

# For this tabs widget, let's conveniently re-use the data from the
# AccordionWidget, but change the third option to load its data via ajax!
ajaxified_tabs_items = [{'label': v[0], 'content': v[1]} for v in some_items]
ajaxified_tabs_items[2]['label'] += ' (via ajax)'
ajaxified_tabs_items[2]['href'] = '/ajaxtab/'
del ajaxified_tabs_items[2]['content']

class DemoTabsWidget(TabsWidget):
    items = ajaxified_tabs_items

    @classmethod
    def request(cls, req):
        # You could, of course, use other controllers (say a tg2 controller)
        import time
        import webob
        time.sleep(1)
        resp = webob.Response(request=req, content_type="text/html")
        resp.body = "<p>wow.. this came via <h4>ajax!</h4></p>"
        return resp

# Register the widget's controller
import tw2.core as twc
try:
    mw = twc.core.request_local()['middleware']
    mw.controllers.register(DemoTabsWidget, 'ajaxtab')
except TypeError as e:
    pass  # This happens if the middleware hasn't been installed.
