import traceback
from unittest import mock


class AdvancedCall(mock._Call):
    """
    An override for the default mock._Call class which adds some additional
    functionality.
    """

    original_call_class = mock._Call

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.where = traceback.format_stack()

    @classmethod
    def apply(cls):
        """
        Apply the override
        """
        mock._Call = cls

    @classmethod
    def unapply(cls):
        """
        Unapply the override
        """
        mock._Call = cls.original_call_class
