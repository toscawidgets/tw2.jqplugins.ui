
# TW2 proper imports
from tw2.core import CSSLink, JSLink
from tw2.core.params import Param
from tw2.core.resources import encoder

# tw2.jquery.core imports
from tw2.jquery.core import JQueryWidget
from tw2.jquery.core.base import jQueryJSLink
from tw2.jquery.core.base import jQueryPluginLinkMixin
from tw2.jquery.core.version import JSLinkMixin

# import from *this* package
from tw2.jquery.ui import defaults

### Links, etc...
class jQueryUIMixin(jQueryPluginLinkMixin):
    dirname = defaults._ui_dirname_
    basename='jquery-ui'
    modname = 'tw2.jquery.ui'

class jQueryUIJSLink(JSLink, jQueryUIMixin):
    subdir = 'js'

class jQueryUIThemeCSSLink(jQueryUIMixin, CSSLink):
    name = Param('(string) Specify the name of the theme that you wish to use.  Default: %s' % defaults._ui_theme_name_, default=defaults._ui_theme_name_)
    @property
    def subdir(self):
        return 'css/%(name)s' % dict(name=self.name)
    extension = 'css'

### Resources
jquery_js = jQueryJSLink()
jquery_ui_css = jQueryUIThemeCSSLink(
    name=defaults._ui_theme_name_, version=defaults._ui_version_)
jquery_ui_js = jQueryUIJSLink(version=defaults._ui_version_)
jquery_ui = jQueryJSLink(resources = [jquery_ui_css, jquery_ui_js])

### Widgets
class JQueryUIWidget(JQueryWidget):
    """ Base JQueryUIWidget """
    resources = [ jquery_js, jquery_ui_js, jquery_ui_css ]

    options = Param(
        '(dict) A dict of options to pass to the widget', default={})

    click = Param('(str) javascript callback for click event', default=None)
    
    def prepare(self):
        self.options = encoder.encode(self.options)
        super(JQueryUIWidget, self).prepare()
