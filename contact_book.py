### Contact book
### An application that allows users to add, search, and delete contacts.


#import time

### Contact book with samples
contactBook = {'John Jo': '555-555-5555', 'Mugi Mu': '556-556-5656', 'Mike Mi' : '554-554-5454', 'Lora Lo' : '557-557-5757'}

def addContact():
    """
    Docstring:
    A function that asks the user for the name and phone number of the contact they want to add and updates the contactBook dictionary accordingly.
    """
    contactName = input('\nEnter first AND last name of contact: ').title() 
    phoneNumber = input('\nEnter phone number: ')
    contactBook.update([(contactName, phoneNumber)])
    print ("\n\nContact has been added\n\n\n")

def searchContact():
    """
    Docstring:
    A function that asks the user for the name of the contact they want to search for, then displays the information of the contact.
    """
    search = input("\nEnter the name of the contact you would like to search for: ").title()
    if search in contactBook:
        print(f"Contact found: {search}, Phone Number: {contactBook[search]}\n\n\n")
        #time.sleep(2)

    else:
        contactFound = False
        for name, phone in contactBook.items():
            if search in name:
                print(f"\nContact found: {name}, Phone Number: {phone}\n\n\n")
                #time.sleep(2)
                contactFound = True
                break
        if not contactFound:
                print ("\n\nContact not found\n")
                #time.sleep(2)

def deleteContact():
    """
    Docstring:
    A function that asks the user for the name of the contact they want to delete, then removes the contact from the contactBook dictionary.
    """
    delete = input("\nEnter the FULL name of contact to delete: ").title()
    if delete in contactBook:
        del contactBook[delete]
        print ("\n\nContact has been deleted\n\n\n")
        #time.sleep(2)
    else:
        contactFound = False
        for name, phone in contactBook.items():
            if delete in name:
                del contactBook[delete]
                print ("\n\nContact has been deleted\n\n\n")
                #time.sleep(2)
                contactFound = True
                break
            if not contactFound:
                print ("\n\nContact not found\n")
                #time.sleep(2)


print ("\n\nContact Book\n")

while True:
    ### Print out the contact book
    for name, phone in contactBook.items():
        print (f"{name}: {phone}")

    ### Ask the user what they want to do
    action = input("\n\n(To exit type exit)\nWould you like to add, search, or delete a contact? ").upper()

    
    if 'ADD' in action:
        addContact()

    elif 'SEARCH' in action:
        searchContact()

    elif 'DELETE' in action:
        deleteContact()
