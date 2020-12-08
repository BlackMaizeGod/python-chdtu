import json

class Student(object):

    def __init__(self, firstName, lastName, middleName, phoneNumber, gender, age):        
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setMiddleName(middleName)
        self.setPhoneNumber(phoneNumber)
        self.setGender(gender)
        self.setAge(age)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getMiddleName(self):
        return self.middleName

    def getPhoneNumber(self):
        return self.phoneNumber

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setMiddleName(self, middleName):
        self.middleName = middleName

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def setGender(self, gender):
        self.gender = gender

    def setAge(self, age):
        self.age = age        

    def getJsonFormattedInfo(self):
        return ({
            "first name": self.getFirstName(),
            "last name": self.getLastName(),
            "middle name": self.getMiddleName(),
            "phone number": self.getPhoneNumber(),
            "gender": self.getGender(),
            "age": self.getAge()
        })
