  
class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self,website_name,username,password):

      # docstring removed for simplicity

        self.username= username
        self.password= password
        self.website_name=website_name
      
 # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    @classmethod
    def credential_exists(cls,website_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            website_name: website_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.website_name == website_name:
                    return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list