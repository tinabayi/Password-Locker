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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []


    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("yahoo.com","bayizerechristine","Kansangire81") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)


    def test_credential_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("facebook.com","bayizerechristine4","wecode2019kie") # new credential
        test_credential.save_credential()

        credential_exist = Credential.credential_exists("facebook.com")

        self.assertTrue(credential_exist)

    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()

            self.new_contact.delete_contact()# Deleting a contact object
            self.assertEqual(len(Contact.contact_list),1)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)


if __name__ == '__main__':
    unittest.main()