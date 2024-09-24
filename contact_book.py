### Contact book
### An application that allows users to add, search, and delete contacts.

'''
class Contact:
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
'''

contactBook = {}

def newContact():
    contactName = input('Enter first and last name of contact: ').title() 
    phoneNumber = input('Enter phone number: ')
    contactBook.update([(contactName, phoneNumber)])
    print ("Contact has been added")

newContact()
print (contactBook)


