import json

class PhoneBook(object):

    def __init__(self, id, firstName, middleName, lastName, homePhone, phoneNumber, additionalInfo):
    	self.setId(id)
    	self.setFirstName(firstName)
    	self.setMiddleName(middleName)
    	self.setLastName(lastName)
    	self.setHomePhone(homePhone)
    	self.setPhoneNumber(phoneNumber)
    	self.setAdditionalInfo(additionalInfo)

    def __del__(self):
        self.exportDataToJson()
        print('Your Data has been exported to json as ' + str(self.getId()) + '.json')

    def setId(self, id):
    	self.id = id

    def setFirstName(self, firstName):
    	self.firstName = firstName
    
    def setMiddleName(self, middleName):
    	self.middleName = middleName
    
    def setLastName(self, lastName):
    	self.lastName = lastName
    
    def setHomePhone(self, homePhone):
    	self.homePhone = homePhone
    
    def setPhoneNumber(self, phoneNumber):
    	self.phoneNumber = phoneNumber
    
    def setAdditionalInfo(self, additionalInfo):
    	self.additionalInfo = additionalInfo
    	
    def getId(self):
    	return self.id
    	
    def getFirstName(self):
    	return self.firstName
    
    def getMiddleName(self):
    	return self.middleName
    
    def getLastName(self):
    	return self.lastName
    
    def getHomePhone(self):
    	return self.homePhone
    
    def getPhoneNumber(self):
    	return self.phoneNumber
    
    def getAdditionalInfo(self):
    	return self.additionalInfo
    
    def getJsonFormattedData(self):
        return ({
            "first name": self.getFirstName(),
            "last name": self.getLastName(),
            "middle name": self.getMiddleName(),
            "home phone": self.getHomePhone(),
            "phone number": self.getPhoneNumber(),
            "additional info": self.getAdditionalInfo()
        })

    def exportDataToJson(self):
        file = open('exported_phonebook_entity/' + str(self.getId()) + '.json', 'w')
        file.write(json.dumps(self.getJsonFormattedData()))
        file.close()
