
import os

contacts = {}
file_name = "contact-book.txt"

if os.path.exists(file_name):
    with open("contact-book.txt", "r") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 2:
                name, number = parts
                contacts[name] = number

def save_contacts():
    # Save contacts dictionary to a file.
    with open(file_name, "w") as f:
        for name, number in contacts.items():
            f.write(f"{name} | {number}\n")

def show_contacts():
    if not contacts:
        print("there is nothing to show you.")
    else:
        for i, (name,number) in enumerate(contacts.items(), start=1):
            print(f"{i}. {name} | {number}")

while True :
    print("-----CONTACT-BOOK----")
    print("1. Add a new contact.")
    print("2. Search for a contact.")
    print("3. Delete a contact.")
    print("4. Edit a contact.")
    print("5. See complete logbook.")
    print("6. Quit program.")
    print("--------------------")

    try:
        option = int(input("What do you want to do? Enter your option: "))
    except ValueError:
        print("Please Enter a valid option number.")
        continue

    if option == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts.update({name:number})
        save_contacts()
        print("Contact details added.")

    elif option == 2:
        if not contacts :
            print("Contact book is empty.")
        else:
            name = input("Enter name of the person: ")
            if name in contacts:
                print(f"contact nummber of {name} is {contacts[name]}")
            else:
                print("Person not found.Try again with correct name.")

    elif option == 3:
        if not contacts:
            print("There is nothing to delete.Logbook is empty.")
        else:
            name = input("Enter name to delete number: ")
            if name in contacts:
                del contacts[name]
                print("contact deleted.") 
                save_contacts()
            else:
                print("Person not found.")

    elif option == 4 :
        if not contacts :
            print("Book is empty. Nothing to update. Try adding new one.")
        else:
            name = input("Enter name : ")
            if name in contacts:                
                number = input ("Enter number : ")
                contacts.update({name :number})
                print("contact updated.")
                save_contacts()
            else:
                print("there isn't any data of the given name.You wanna make new one?")

    elif option == 5:
        if not contacts:
            print("oops.. Empty book. Trying adding new one.")
        else:
            show_contacts()

    elif option == 6 :
        print("bye bye.. try another time.")
        break

    else:
        print("Try a valid option.")