import tw2.jquery.core as twjqc
from tw2.jquery.ui import resources as res

import tw2.core as twc
from tw2.core.resources import encoder

# TODO make a base class JQueryUIWidget that knows how to apply all the right css tags to make widgets compliant.
# TODO have base widget handle resources too
# TODO prepare methods should verify data before rendering
# TODO doc strings should fully match http://jqueryui.com/demos/
# TODO use generic 'options' param to handle all options ^^

class AccordianWidget(twjqc.JQueryWidget):
    """
    Click headers to expand/collapse content that is broken into
    logical sections, much like tabs. Optionally, toggle sections
    open/closed on mouseover.

    The underlying HTML markup is a series of headers (H3 tags) and
    content divs so the content is usable without JavaScript.
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.accordian"

    # TODO -- use strings or widgets or Markup or what?
    # TODO -- if strings, how to unescape HTML?
    items = twc.Param(
        'A list of (header (str), content (str)) tuples', default=[])

class AutocompleteWidget(twjqc.JQueryWidget):
    """
    The Autocomplete widgets provides suggestions while you type into
    the field. Here the suggestions are tags for programming languages,
    give "ja" (for Java or JavaScript) a try.

    The datasource is a simple JavaScript array, provided to the widget
    using the source-option.
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.autocomplete"

    tags = twc.Param('List of completable strings', default=[])

    def prepare(self):
        super(AutocompleteWidget, self).prepare()
        self.tags = encoder.encode(self.tags)

class ButtonWidget(twjqc.JQueryWidget):
    """ A button with a javascript callback with different markup flavors. """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.button"

    type = twc.Param(
        'Type of button.  Valid values are "button", "input", "anchor"',
        default='button')

    value = twc.Param('Value of the label on the button')

    js_callback = twc.Param(
        'A string describing a javascript callback',
        default='function() { return false; }'
    )

class DatePickerWidget(twjqc.JQueryWidget):
    """
    The datepicker is tied to a standard form input field.
    Focus on the input (click, or use the tab key) to open an
    interactive calendar in a small overlay.  Choose a date, click
    elsewhere on the page (blur the input), or hit the Esc key to
    close.  If a date is chosen, feedback is shown as the input's
    value.
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.datepicker"

class DialogWidget(twjqc.JQueryWidget):
    """
    The basic dialog window is an overlay positioned within the
    viewport and is protected from page content (like select elements)
    shining through with an iframe. It has a title bar and a content
    area, and can be moved, resized and closed with the 'x' icon by default.

    It is likely displayed at the top of the page right now ;p
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.dialog"
    title = twc.Param('The title for the dialog', attribute=True)
    value = twc.Param('The message for the dialog')

class ProgressBarWidget(twjqc.JQueryWidget):
    """
    The progress bar is designed to simply display the current % complete
    for a process. The bar is coded to be flexibly sized through CSS and
    will scale to fit inside it's parent container by default.
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.progressbar"
    value = twc.Param('Value of the progress bar')

class SliderWidget(twjqc.JQueryWidget):
    """
    The jQuery UI Slider plugin makes selected elements into sliders.
    There are various options such as multiple handles, and ranges. The
    handle can be moved with the mouse or the arrow keys.
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.slider"

class TabsWidget(twjqc.JQueryWidget):
    """
    Tabs are generally used to break content into multiple sections that
    can be swapped to save space, much like an accordion.

    By default a tab widget will swap between tabbed sections onClick, but
    the events can be changed to onHover through an option. Tab content can
    be loaded via Ajax by setting an href on a tab.
    """
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.tabs"
    items = twc.Param(
        'A list of (header (str), content (str)) tuples', default=[])
