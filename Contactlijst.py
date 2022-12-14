def start_message():
    print("\n"
          "Hallo, dit is uw contactlijst.\n"
          "Typ 1 om jouw contacten te bekijken\n"
          "Typ 2 om een contact toe te voegen\n"
          "Typ 3 om een contact aan te passen\n"
          "Typ 4 om een contact te verwijderen\n"
          "Typ 5 om dit programma te sluiten\n")

def contact_view(contacten):
    print(contacten)

def contact_add(contacten):
    name = str(input("Naam van contact: "))
    phone_number = input("Telefoonnummer van contact: ")
    if name in contacten:
        print("\n""Dit contact bestaat al ")
    else:
        contacten[name] = phone_number

def contact_edit(contacten):
    selected_contact = str(input("Wat is de naam van het contact dat je wilt editen? "))
    if selected_contact not in contacten:
        print("\n""Dit contact bestaat niet")
    else:
        del contacten[selected_contact]
        name = str(input("Nieuwe naam van contact: "))
        phone_number = str(input("Nieuwe telefoonnummer van contact: "))
        if name in contacten:
            print("\n""Dit contact bestaat al")
        else:
            contacten[name] = phone_number

def contact_remove(contacten):
    selected_contact = str(input("Wat is de naam van het contact dat je wilt verwijderen? "))
    if selected_contact not in contacten:
        print("\n""Dit contact bestaat niet")
    else:
        del contacten[selected_contact]

def select():
    selected = int(input())
    return selected

def program():
    contacten = {}
    selected = 0
    while selected != 5:
        start_message()
        selected = select()
        if (selected == 1):
            contact_view(contacten)
        elif (selected == 2):
            contact_add(contacten)
        elif (selected == 3):
            contact_edit(contacten)
        elif (selected == 4):
            contact_remove(contacten)

program()
