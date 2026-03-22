contact = {}

def addcontact():
    name = input("Enter the name: ")
    number = input("Enter the number: ")

    if name in contact:
        print("Contact already exists")
    else:
        contact[name] = number
        print("Contact added")


def deletecontact():
    name = input("Enter the name: ")

    if name in contact:
        del contact[name]
        print("Deleted successfully")
    else:
        print("Contact not found")


def viewcontact():
    if not contact:
        print("No contacts available")
    else:
        for name, number in contact.items():
            print(name, ":", number)


def searchcontact():
    name = input("Enter the name: ")

    if name in contact:
        print("Found :", contact[name])
    else:
        print("Contact not found ")


#  Main Menu Loop
while True:
    print("\n--- MENU ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Search Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addcontact()
    elif choice == "2":
        deletecontact()
    elif choice == "3":
        viewcontact()
    elif choice == "4":
        searchcontact()
    elif choice == "5":
        print("Exiting... ")
        break
    else:
        print("Invalid choice ")