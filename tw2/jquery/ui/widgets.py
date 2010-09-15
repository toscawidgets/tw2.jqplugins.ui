from tw2.jquery.core.base import jQueryJSLink
from tw2.jquery.ui.base import jQueryUIThemeCSSLink, jQueryUIJSLink
import defaults

jquery_js = jQueryJSLink()

# Note we use the default smoothness theme
jquery_ui_css = jQueryUIThemeCSSLink(name=defaults._ui_theme_name_, version=defaults._ui_version_)
jquery_ui_js = jQueryUIJSLink(version=defaults._ui_version_)

jquery_ui = jQueryJSLink(resources = [jquery_ui_css, jquery_ui_js])

