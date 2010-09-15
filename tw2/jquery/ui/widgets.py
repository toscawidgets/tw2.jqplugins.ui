from tw2.jquery.core.base import jQueryJSLink
from tw2.jquery.core.widgets import JQueryWidget
from tw2.jquery.ui.base import jQueryUIThemeCSSLink, jQueryUIJSLink
from tw2.jquery.ui import defaults

from tw2.core.resources import encoder
import tw2.core as twc

jquery_js = jQueryJSLink()

# Note we use the default smoothness theme
jquery_ui_css = jQueryUIThemeCSSLink(name=defaults._ui_theme_name_, version=defaults._ui_version_)
jquery_ui_js = jQueryUIJSLink(version=defaults._ui_version_)

jquery_ui = jQueryJSLink(resources = [jquery_ui_css, jquery_ui_js])

# TODO http://jqueryui.com/demos/
class AccordianWidget(JQueryWidget):
    """
    Click headers to expand/collapse content that is broken into
    logical sections, much like tabs. Optionally, toggle sections
    open/closed on mouseover.

    The underlying HTML markup is a series of headers (H3 tags) and
    content divs so the content is usable without JavaScript.
    """

    resources = [
        jquery_js,
        jquery_ui_js,
        jquery_ui_css,
    ]

    template = "tw2.jquery.ui.templates.accordian"

    # TODO -- use strings or widgets or Markup or what?
    items = twc.Param(
        'A list of (header (str), content (str)) tuples', default=[])

class AutocompleteWidget(JQueryWidget):
    """
    The Autocomplete widgets provides suggestions while you type into
    the field. Here the suggestions are tags for programming languages,
    give "ja" (for Java or JavaScript) a try.

    The datasource is a simple JavaScript array, provided to the widget
    using the source-option.
    """

    resources = [
        jquery_js,
        jquery_ui_js,
        jquery_ui_css,
    ]

    template = "tw2.jquery.ui.templates.autocomplete"

    tags = twc.Param('List of completable strings', default=[])
    def prepare(self):
        super(AutocompleteWidget, self).prepare()
        self.tags = encoder.encode(self.tags)

