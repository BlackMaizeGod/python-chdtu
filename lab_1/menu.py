import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from PhoneBook import PhoneBook
from random import randrange

if __name__ == '__main__':
    firstName = input('First Name: ')
    secondName = input('Second Name: ')
    middleName = input('Midle Name: ')
    homePhone = input('Home Phone: ')
    phoneNumber = input('Phone Number: ')
    additionalInfo = input('Other Info: ')
    
    phoneBook = PhoneBook(randrange(999999999),firstName, secondName, middleName, homePhone, phoneNumber, additionalInfo)
    
    del phoneBook


