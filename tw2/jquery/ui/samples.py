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
    value = "This is a jQuery UI button"
    click = "function() { alert( 'Hello world!' ) }"

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
    value = 28

class DemoSliderWidget(SliderWidget):
    pass

class DemoTabsWidget(TabsWidget):
    items = some_items
