#!/usr/bin/env python3.6
from user import User
from credentials import Credential
def create_user(first_name,last_name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,username,password)
    return new_user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user() 

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_credentials(website_name,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(website_name,username,password)
    return new_credential


def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credentials()

def check_existing_credentials(username):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential() 


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def main():

    # print("Hello Welcome . What is your first_name?")
    # first_name = input()
    # print( "What is your last_name")
    # last_name=input()

    while True:
        print("Use these short codes : cc - create a new user, dc - display credentias, fd -find a credential, ex -exit the credential list ")
        short_code = input().lower()
        if short_code == 'cc':
                print ("First name ....")
                first_name = input()
                print("Last name ...")
                last_name = input()
                print ("username ....")
                username = input()
                print("Password...")
                password = input()
                save_users(create_user(first_name,last_name,username,password)) # create and save new user.
                print ('\n')
                print(f"New User {first_name} {last_name}{username} {password} created")
                print ('\n')

        elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.website_name} {credential.username} .....{credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

        elif short_code == 'fd':
            
            print("username")

            username = input()
            if check_existing_credentials(username):
                  search_credential = find_credential(username)
                  print(f"{search_credential.username} {search_credential.password}")
                  print('-' * 20)
         
            else:
                 print("That credential does not exist")

        elif short_code == "ex":
                 print("Bye .......")
                 break
        else:
                print("I really didn't get that. Please use the short codes")
   
if __name__ == '__main__':

    main()
