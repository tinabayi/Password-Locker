#!/usr/bin/env python3.6
from user import User
def create_user(first_name,last_name,username,passward):
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

def check_existing_credentials(website_name):
    '''
    Function that check if a credential exists with that website_name and return a Boolean
    '''
    return Credential.credential_exist(websit_name)
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

    print("Hello Welcome . What is your first_name?")
    first_name = input()
    print( "What is your last_name")
    last_name=input()
    print(f"{first_name},type your username")
    user_name=input()
    print("Your password ?")
    passward=input()
if __name__ == '__main__':

    main()
