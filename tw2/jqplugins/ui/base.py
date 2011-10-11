# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery imports
from tw2.jquery.base import jQueryJSLink, jQueryPluginLinkMixin
from tw2.jquery.version import JSLinkMixin
from tw2.jquery import jquery_js

# import from *this* package
import defaults

### Links, etc...
class jQueryUIMixin(jQueryPluginLinkMixin):
    dirname = defaults._ui_dirname_
    basename='jquery-ui'
    modname = 'tw2.jqplugins.ui'

class jQueryUIJSLink(twc.JSLink, jQueryUIMixin):
    subdir = 'js'

class jQueryUIThemeCSSLink(jQueryUIMixin, twc.CSSLink):
    name = twc.Variable()  # Generated from get_ui_theme_name()

    @property
    def subdir(self):
        return 'css/%(name)s' % dict(name=self.name)
    extension = 'css'

    def prepare(self):
        self.name = get_ui_theme_name()
        super(jQueryUIThemeCSSLink, self).prepare()

def set_ui_theme_name(ui_theme_name):
    """ Set the jquery ui theme on a request/thread local basis 

    Using Supported Themes
    ----------------------

    Supported themes live in ``tw2/jqplugins/ui/static/jquery/ui/version/css``

    At present they include

    - blitzer
    - cupertino
    - dark-hive
    - eggplant
    - excite-bike
    - flick
    - hot-sneaks
    - humanity
    - le-frog
    - overcast
    - pepper-grinder
    - redmond
    - smoothness
    - south-street
    - start
    - sunny
    - ui-darkness
    - ui-lightness
    - vader

    Installing Your Own Theme
    -------------------------

    You could in theory install your own theme called, say, ``my-theme``.
    The best way of doing this would be to build your theme with the jquery
    ui `ThemeRoller <http://jqueryui.com/themeroller/>`_ and install it inside
    your project.  Create a symlink pointing from
    ``tw2/jqplugins/ui/static/jquery/ui/version/css/my-theme`` to the directory
    where the theme is really held.  Then, at the beginning of each request
    to your project, make the call ``set_ui_theme_name('my-theme')``

    """
    twc.core.request_local()['jquery_ui_theme_name'] = ui_theme_name

def get_ui_theme_name():
    """ Get the request/thread local jquery ui theme name """
    if 'jquery_ui_theme_name' not in twc.core.request_local():
        base = defaults._ui_theme_name_
        twc.core.request_local()['jquery_ui_theme_name'] = base
    return twc.core.request_local()['jquery_ui_theme_name']

### Resources
jquery_ui_css = jQueryUIThemeCSSLink(version=defaults._ui_version_)
jquery_ui_catcomplete_js = jQueryUIJSLink(version='custom',
                                          basename='catcomplete')
jquery_ui_js = jQueryUIJSLink(version=defaults._ui_version_,
                              resources=[jquery_js])
jquery_ui = jQueryJSLink(resources = [jquery_ui_css, jquery_ui_js])


### Widgets
class JQueryUIWidget(twc.Widget):
    """ Base JQueryUIWidget """
    _hide_docs = False
    resources = [ jquery_ui_js, jquery_ui_css ]

    jqmethod = twc.Variable("(str) Name of this widget's jQuery init method")
    selector = twc.Variable("(str) Escaped id.  jQuery selector.")

    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})

    # TODO -- add all the events http://api.jquery.com/category/events/
    # TODO -- try to automatically generate IDs if not specified
    # TODO -- TBD, figure out if this actually makes sense for all ui things.

    events = twc.Param(
        '(dict) (BETA) javascript callbacks for events', default={})

    def prepare(self):
        if self.events is not None and not isinstance(self.events, dict):
            raise ValueError, 'Events parameter must be a dict'

        self.resources.append(jquery_ui_css(name=get_ui_theme_name()))
        self.options = encoder.encode(self.options)
        super(JQueryUIWidget, self).prepare()
        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError, 'JQueryWidget must be supplied an id'
        self.selector = self.attrs['id'].replace(':', '\\\\:')
