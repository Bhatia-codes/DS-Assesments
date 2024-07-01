phone_book = {}  

def add_contact():

    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    if name in phone_book:
        phone_book[name].append(phone_number)
    else:
        phone_book[name] = [phone_number]
    print(f"Contact {name} added successfully!")

def search_contact():

    name = input("Enter the name to search: ")
    if name in phone_book:
        print(f"Phone numbers of {name} are {(phone_book[name])}")
    else:
        print(f"No contact found with name {name}")

def delete_contact():

    name = input("Enter the name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with name {name}")

def delete_phone():

    name = input("Enter the name: ")
    phone_number = input("Enter the phone number to delete: ")
    if name in phone_book:
        if phone_number in phone_book[name]:
            phone_book[name].remove(phone_number)
            print(f"Phone number {phone_number} deleted successfully!")
        else:
            print(f"No phone number {phone_number} found for {name}")
    else:
        print(f"No contact found with name {name}")

def display_contacts():

    if phone_book:
        print("Phone Book:")
        for name, phone_numbers in phone_book.items():
            print(f"{name}: {phone_numbers}")
    else:
        print("Phone book is empty!")

while True:
    print("\nPhone Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Delete Phone Number")
    print("5. Display Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        delete_phone()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again!")