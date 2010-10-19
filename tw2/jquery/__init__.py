__import__('pkg_resources').declare_namespace(__name__)
try:
    from widgets import *
except ImportError, e:
    pass
