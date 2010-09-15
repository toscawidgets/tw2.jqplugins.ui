import tw2.jquery.core as twjqc
from tw2.jquery.ui import resources as res

import tw2.core as twc
from tw2.core.resources import encoder

# TODO http://jqueryui.com/demos/
class AccordianWidget(twjqc.JQueryWidget):
    """
    Click headers to expand/collapse content that is broken into
    logical sections, much like tabs. Optionally, toggle sections
    open/closed on mouseover.

    The underlying HTML markup is a series of headers (H3 tags) and
    content divs so the content is usable without JavaScript.
    """
    # TODO -- go through the different examples to broaden what can be done.
    resources = [ res.jquery_js, res.jquery_ui_js, res.jquery_ui_css ]
    template = "tw2.jquery.ui.templates.accordian"

    # TODO -- use strings or widgets or Markup or what?
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
    




