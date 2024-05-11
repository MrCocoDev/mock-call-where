from unittest import mock

from mock_call_where.override import AdvancedCall


def test_mock_call_has_a_where(mock_where):
    my_mock = mock.Mock()
    my_mock.a_function()
    the_call = my_mock.mock_calls[0]

    assert hasattr(the_call, "where")
    assert type(the_call) is AdvancedCall
    assert (
        "in test_mock_call_has_a_where\n    my_mock.a_function()\n"
        in the_call.where[-4]
    )
