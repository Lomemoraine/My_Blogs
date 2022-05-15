import unittest
from app.models import Subscribe

class SubscribeTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        setup up method that will run before every test
        '''
        self.new_subcriber = Subscribe(email='simotwo@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_subcriber, Subscribe))