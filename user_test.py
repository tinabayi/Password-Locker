import unittest # Importing the unittest module
from user import User #import the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("christine","bayizere","tinabayi","wecode2019kie") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"christine")
        self.assertEqual(self.new_user.last_name,"bayizere")
        self.assertEqual(self.new_user.username,"tinabayi")
        self.assertEqual(self.new_user.password,"wecode2019kie")


if __name__ == '__main__':
    unittest.main()