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


def test_exception_notalist():
    w = tw2.jqplugins.ui.TabsWidget(id='foobar', items='whatevah')
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'items must be of type list')

def test_exception_noid():
    w = tw2.jqplugins.ui.TabsWidget(items=['foo1'])
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'JQueryWidget must be supplied an id')
