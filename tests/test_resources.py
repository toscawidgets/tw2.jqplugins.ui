from __future__ import print_function
import tw2.core as twc
import tw2.jqplugins.ui
from . import testapi

from nose.tools import eq_

js = twc.JSLink(link='paj')
css = twc.CSSLink(link='joe')
csssrc = twc.CSSSource(src='.bob { font-weight: bold; }')
jssrc = twc.JSSource(src='bob')

html = "<html><head><title>a</title></head><body>hello</body></html>"


def simple_app(environ, start_response):
    req = wo.Request(environ)
    ct = 'text/html' if req.path == '/' else 'test/plain'
    resp = wo.Response(request=req, content_type="%s; charset=UTF8" % ct)
    resp.body = html
    return resp(environ, start_response)

mw = twc.make_middleware(simple_app)


def setup():
    testapi.setup()


def test_weird_case_for_zykes():
    rl = testapi.request(1, mw)
    tw2.jqplugins.ui.jquery_ui.inject()

    rl = twc.core.request_local()
    r = rl['resources']
    import pprint
    pprint.pprint(rl['resources'])
    for r in rl['resources']:
        print('-', r)
    eq_(len(rl['resources']), 3)
