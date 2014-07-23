import random
import unittest

from kite import Template

class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.public_key = '7ea493ad22d5930f753cf40e9df9b254bc086a77'
        # Make sure these are test credentials.
        self.secret_key = 'a8f99f40c29cc677d1740c322720aa3d9243c43a'
        # Make sure these are test credentials.

    def test_get_cost(self):
        kite = Template("polaroids", self.public_key, self.secret_key)
        cost = kite.get_cost(currency="EUR")
        self.assertEquals(cost, {
            'amount': "5.00",
            'currency': "EUR",
            'minimum': "5.00"
            })
##        cost = kite.get_cost(currency="USD")
##        self.assertEquals(cost, {
##            'amount': "7.00",
##            'currency': "USD",
##            'minimum': "7.00"
##            })
##        cost = kite.get_cost(currency="GBP")
##        self.assertEquals(cost, {
##            'amount': "4.00",
##            'currency': "GBP",
##            'minimum': "4.00"
##            })

if __name__ == '__main__':
    unittest.main()
