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
