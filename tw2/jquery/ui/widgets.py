
# tw2-proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# imports from this package
from tw2.jquery.ui import base as uibase

### List of TODOs
# TODO prepare methods should verify data before rendering
# TODO doc strings should fully match http://jqueryui.com/demos/
# TODO use generic 'options' param to handle all options ^^

class AccordianWidget(uibase.JQueryUIWidget):
    """
    Click headers to expand/collapse content that is broken into
    logical sections, much like tabs. Optionally, toggle sections
    open/closed on mouseover.

    The underlying HTML markup is a series of headers (H3 tags) and
    content divs so the content is usable without JavaScript.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/accordion/

    description of supported options:
        disabled -- boolean (default: False)

        active -- selector, element, jQuery, boolean, number (default: first child)

        animated -- boolean, str (default: 'slide')

        autoHeight -- boolean (default: True)

        clearStyle -- boolean (default: False)

        collapsible -- boolean (default: False)

        event -- str (default: 'click')

        fillSpace -- boolean (default: False)

        header -- selector, jQuery (default: '> li > :first-child,> :not(li):even')

        icons -- dict (default: {'header': 'ui-icon-triangle-1-e', 'headerSelected': 'ui-icon-triangle-1-s'})

        navigation -- boolean (default: False)

        navigationFilter -- javascript string (default: '')

    """

    template = "tw2.jquery.ui.templates.accordian"

    # TODO -- use strings or widgets or Markup or what?
    # TODO -- if strings, how to unescape HTML?
    items = twc.Param(
        'A list of (header (str), content (str)) tuples', default=[])

class AutocompleteWidget(uibase.JQueryUIWidget):
    """
    The Autocomplete widgets provides suggestions while you type into
    the field. Here the suggestions are tags for programming languages,
    give "ja" (for Java or JavaScript) a try.

    The datasource is a simple JavaScript array, provided to the widget
    using the source-option.

    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/autocomplete/

    description of supported options:

        disabled -- boolean (default: False)

        delay -- int (default: 300)

        minLength -- int (default: 1)

        source -- str, list, callback (default: None)
    """
    template = "tw2.jquery.ui.templates.autocomplete"

    def prepare(self):
        super(AutocompleteWidget, self).prepare()

class ButtonWidget(uibase.JQueryUIWidget):
    """
    A button with a javascript callback with different markup flavors.

    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/button/

    description of supported options:

        disabled -- boolean (default: False)

        text -- boolean (default: True)

        icons -- dict (default: {'primary' : None, 'secondary' : None})

        label -- str (default: "HTML content of the button")

    """
    template = "tw2.jquery.ui.templates.button"

    type = twc.Param(
        'Type of button.  Valid values are "button", "input", "anchor"',
        default='button')

class DatePickerWidget(uibase.JQueryUIWidget):
    """
    The datepicker is tied to a standard form input field.
    Focus on the input (click, or use the tab key) to open an
    interactive calendar in a small overlay.  Choose a date, click
    elsewhere on the page (blur the input), or hit the Esc key to
    close.  If a date is chosen, feedback is shown as the input's
    value.
    """
    template = "tw2.jquery.ui.templates.datepicker"

class DialogWidget(uibase.JQueryUIWidget):
    """
    The basic dialog window is an overlay positioned within the
    viewport and is protected from page content (like select elements)
    shining through with an iframe. It has a title bar and a content
    area, and can be moved, resized and closed with the 'x' icon by default.

    It is likely displayed at the top of the page right now ;p
    """
    template = "tw2.jquery.ui.templates.dialog"
    title = twc.Param('The title for the dialog', attribute=True)
    value = twc.Param('The message for the dialog')

class ProgressBarWidget(uibase.JQueryUIWidget):
    """
    The progress bar is designed to simply display the current % complete
    for a process. The bar is coded to be flexibly sized through CSS and
    will scale to fit inside it's parent container by default.
    """
    template = "tw2.jquery.ui.templates.progressbar"
    value = twc.Param('Value of the progress bar')

class SliderWidget(uibase.JQueryUIWidget):
    """
    The jQuery UI Slider plugin makes selected elements into sliders.
    There are various options such as multiple handles, and ranges. The
    handle can be moved with the mouse or the arrow keys.
    """
    template = "tw2.jquery.ui.templates.slider"

class TabsWidget(uibase.JQueryUIWidget):
    """
    Tabs are generally used to break content into multiple sections that
    can be swapped to save space, much like an accordion.

    By default a tab widget will swap between tabbed sections onClick, but
    the events can be changed to onHover through an option. Tab content can
    be loaded via Ajax by setting an href on a tab.
    """
    template = "tw2.jquery.ui.templates.tabs"
    items = twc.Param(
        'A list of (header (str), content (str)) tuples', default=[])
