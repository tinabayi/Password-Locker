import unittest # Importing the 
from credentials import Credential

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("facebook.com","christinebayizere","kansangire81") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.website_name,"facebook.com")
        self.assertEqual(self.new_credential.username,"christinebayizere")
        self.assertEqual(self.new_credential.password,"kansangire81")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    


if __name__ == '__main__':
    unittest.main()