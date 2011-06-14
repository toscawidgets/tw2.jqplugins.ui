import tw2.core as twc
import tw2.jqplugins.ui


def request_local_tst():
    global _request_local, _request_id
#    if _request_id is None:
#        raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_set_theme():
    tw2.jqplugins.ui.set_ui_theme_name('vader')
    assert(tw2.jqplugins.ui.get_ui_theme_name() == 'vader')
    w = tw2.jqplugins.ui.TabsWidget(id='foobar', items=[{'name':'awesome'}])
    w.display()
    assert(any(['vader' in r.req().link for r in w.resources]))

def test_set_non_theme():
    tw2.jqplugins.ui.set_ui_theme_name('vader')
    tw2.jqplugins.ui.set_ui_theme_name('smoothness')
    w = tw2.jqplugins.ui.TabsWidget(id='foobar', items=[{'name':'awesome'}])
    w.display()
    assert(not any(['vader' in r.req().link for r in w.resources]))
