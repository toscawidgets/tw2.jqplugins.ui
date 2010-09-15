from tw2.core.params import Param
from tw2.core import CSSLink, JSLink
from tw2.jquery.core.version import JSLinkMixin

import defaults

from tw2.jquery.core.base import jQueryPluginLinkMixin

class jQueryUIMixin(jQueryPluginLinkMixin):
    dirname = defaults._ui_dirname_
    basename='jquery-ui'

class jQueryUIJSLink(JSLink, jQueryUIMixin):
    subdir = 'js'

class jQueryUIThemeCSSLink(jQueryUIMixin, CSSLink):
    name = Param('(string) Specify the name of the theme that you wish to use.  Default: %s' % defaults._ui_theme_name_, default=defaults._ui_theme_name_)
    @property
    def subdir(self):
        return 'css/%(name)s' % dict(name=self.name)
    extension = 'css'

