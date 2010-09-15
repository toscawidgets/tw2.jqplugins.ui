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

    resources = [
        res.jquery_js,
        res.jquery_ui_js,
        res.jquery_ui_css,
    ]

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

    resources = [
        res.jquery_js,
        res.jquery_ui_js,
        res.jquery_ui_css,
    ]

    template = "tw2.jquery.ui.templates.autocomplete"

    tags = twc.Param('List of completable strings', default=[])
    def prepare(self):
        super(AutocompleteWidget, self).prepare()
        self.tags = encoder.encode(self.tags)

