from unittest import TestCase
from ..gib2u import GhebbrishConverter


class TestGhebbrishConverter(TestCase):
    gib = GhebbrishConverter('')

    def test_gibberish_to_utf8_converter(self):
        original_string = "ùìåí çðåê"
        expected_output = "שלום חנוך"
        self.assertEqual(self.gib.convert_gibberish_to_utf8(original_string), expected_output)
