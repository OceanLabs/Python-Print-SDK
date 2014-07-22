import random
import unittest

from kite.kite import Template

class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.public_key = ''  # Make sure these are test credentials
        self.secret_key = ''  # Make sure these are test credentials

    def test_get_and_edit_template(self):
        kite = Template(id="polaroids")
        cost = kite.get_cost("EUR")
        self.assertEquals(cost, 2.50)

if __name__ == '__main__':
    unittest.main()