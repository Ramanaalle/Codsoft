import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):

  
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone_number']]

    if not found_contacts:
        print("No contacts found.")
        return

    for contact in found_contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone_number']:
            print(f"Current details - Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")
            
            contact['name'] = input("Enter new name : ") or contact['name']
            contact['phone_number'] = input("Enter new phone number : ") or contact['phone_number']
            contact['email'] = input("Enter new email : ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    
    print("Contact not found.")


def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if search_term in contact['name'] or search_term in contact['phone_number']:
            del contacts[i]
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    
    print("Contact a not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n--------CONTACT MANAGEMENT SYSTEM--------")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
