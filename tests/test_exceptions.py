from __future__ import print_function

import tw2.core as twc
import tw2.jqplugins.ui

from nose.tools import raises


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


@raises(ValueError)
def test_exception_notalist():
    w = tw2.jqplugins.ui.TabsWidget(id='foobar', items='whatevah')
    w.display()


@raises(ValueError)
def test_exception_noid():
    w = tw2.jqplugins.ui.TabsWidget(items=['foo1'])
    w.display()


@raises(ValueError)
def test_exception_radio_notalist():
    w = tw2.jqplugins.ui.ButtonSetRadio(id='lol', items='fail')
    w.display()


@raises(ValueError)
def test_exception_check_notalist():
    w = tw2.jqplugins.ui.ButtonSetCheckbox(id='lol', items='fail')
    w.display()


def test_non_events_dict():
    w = tw2.jqplugins.ui.ButtonSetCheckbox(id='lol', items=['lol'],
                                           events='failboat')
    try:
        w.display()
        assert(False)
    except ValueError as e:
        print(str(e))
        assert(str(e) == "Events parameter must be a dict")


def test_exception_radio_mischeck():
    w = tw2.jqplugins.ui.ButtonSetRadio(
        id='lol',
        items=[{'id':'foo'}],
        checked_item='bar'
    )
    try:
        w.display()
        assert(False)
    except ValueError as e:
        print(str(e))
        assert(str(e) == "A 'checked_item' has been passed in but the id to "+
                         "which it refers is not in the 'items' list" )
