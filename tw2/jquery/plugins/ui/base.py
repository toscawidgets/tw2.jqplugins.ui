
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery imports
from tw2.jquery.base import jQueryJSLink, jQueryPluginLinkMixin
from tw2.jquery.version import JSLinkMixin

# import from *this* package
from tw2.jquery.plugins.ui import defaults

### Links, etc...
class jQueryUIMixin(jQueryPluginLinkMixin):
    dirname = defaults._ui_dirname_
    basename='jquery-ui'
    modname = 'tw2.jquery.plugins.ui'

class jQueryUIJSLink(twc.JSLink, jQueryUIMixin):
    subdir = 'js'

class jQueryUIThemeCSSLink(jQueryUIMixin, twc.CSSLink):
    name = twc.Param('(string) Specify the name of the theme that you wish to use.  Default: %s' % defaults._ui_theme_name_, default=defaults._ui_theme_name_)
    @property
    def subdir(self):
        return 'css/%(name)s' % dict(name=self.name)
    extension = 'css'

### Resources
jquery_js = jQueryJSLink()
jquery_ui_css = jQueryUIThemeCSSLink(
    name=defaults._ui_theme_name_, version=defaults._ui_version_)
jquery_ui_catcomplete_js = jQueryUIJSLink(version='custom',
                                          basename='catcomplete')
jquery_ui_js = jQueryUIJSLink(version=defaults._ui_version_)
jquery_ui = jQueryJSLink(resources = [jquery_ui_css, jquery_ui_js])

### Widgets
class JQueryUIWidget(twc.Widget):
    """ Base JQueryUIWidget """
    resources = [ jquery_js, jquery_ui_js, jquery_ui_css ]

    jqmethod = twc.Variable("(str) Name of this widget's jQuery init method")

    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})

    # TODO -- add all the events http://api.jquery.com/category/events/
    # TODO -- try to automatically generate IDs if not specified
    click = twc.Param(
        '(str) javascript callback for generic click event', default=None)
    
    def prepare(self):
        self.options = encoder.encode(self.options)
        super(JQueryUIWidget, self).prepare()
        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError, 'JQueryWidget must be supplied an id'
        self.attrs['id'] = self.attrs['id'].replace(':', '-')
