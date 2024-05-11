import pytest

from mock_call_where.override import AdvancedCall


@pytest.fixture
def mock_where():
    """
    Applies the advanced Call class for the duration of a test, this
    way it is only applied when needed and shouldn't impact other tests.
    """
    AdvancedCall.apply()

    yield

    AdvancedCall.unapply()
