### Contact book
### An application that allows users to add, search, and delete contacts.

import time


contactBook = {'John Jo': '555-555-5555', 'Mugi Mu': '556-556-5656', 'Mike Mi' : '554-554-5454', 'Lora Lo' : '557-557-5757'}

def addContact():
    contactName = input('\nEnter first and last name of contact: ').title() 
    phoneNumber = input('\nEnter phone number: ')
    contactBook.update([(contactName, phoneNumber)])
    print ("\n\nContact has been added\n\n\n")

def searchContact():
    search = input("\nEnter name of contact: ").title()
    if search in contactBook:
        print(f"Contact found: {search}, Phone Number: {contactBook[search]}\n\n\n")

    else:
        contactFound = False
        for name, phone in contactBook.items():
            if search in name:
                print(f"\nContact found: {name}, Phone Number: {phone}\n\n\n")
                contactFound = True
                break
        if not contactFound:
                print ("\n\nContact not found\n")



print ("\n\nContact Book\n")

while True:

    for name, phone in contactBook.items():
        print (f"{name}: {phone}")

    action = input("\n\n(To exit type exit)\nWould you like to add, search, or delete a contact? ").upper()

    
    if 'ADD' in action:
        addContact()
    elif 'SEARCH' in action:
        searchContact()

    '''
    elif 'DELETE' in action:

    else:
        quit()
    '''

