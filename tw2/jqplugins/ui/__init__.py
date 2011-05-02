""" TW2 wrapper for the widgets from jquery UI (http://jqueryui.com)

You can set the jquery-ui theme with
``tw2.jqplugins.ui.base.set_ui_theme_name``.  The docstring of that function lists supported themes.

Get the source from http://github.com/ralphbean/tw2.jqplugins.ui
"""

from base import (
    set_ui_theme_name, get_ui_theme_name,
    jquery_ui_js, jquery_ui_css, jquery_ui
)

from widgets import *
