# Upon installation of any of tw2.jquery.plugins.*, this
#   file (originally in tw2.jquery) will be overwritten and
#   therefore must be the same as in tw2.jquery proper.
__import__('pkg_resources').declare_namespace(__name__)
try:
    from widgets import *
except ImportError:
    pass
