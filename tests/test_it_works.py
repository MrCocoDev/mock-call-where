from unittest import mock

from mock_call_where.override import AdvancedCall


def test_mock_call_has_a_where(mock_where):
    my_mock = mock.Mock()
    my_mock.a_function()
    the_call = my_mock.mock_calls[0]

    assert type(the_call) is AdvancedCall
    assert (
        "in test_mock_call_has_a_where\n    my_mock.a_function()\n"
        in the_call.where[-4]
    )


def test_advanced_call_is_not_automatically_applied():
    my_mock = mock.Mock()

    my_mock.a_function()
    call1 = my_mock.mock_calls[0]
    assert type(call1) is mock._Call

    AdvancedCall.apply()

    my_mock.another_function()
    call2 = my_mock.mock_calls[1]
    assert type(call2) is AdvancedCall

    AdvancedCall.unapply()

    my_mock.a_third_function()
    call3 = my_mock.mock_calls[2]
    assert type(call3) is mock._Call
