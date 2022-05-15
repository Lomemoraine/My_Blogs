import unittest
from app.models import Quote

class QuoteSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        setup up method that will run before every test
        '''
        self.new_quote = Quote('Charles Dawson','Tech is great')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))