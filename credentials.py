  
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
       