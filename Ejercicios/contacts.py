# -*- coding: utf-8 -*-
import csv
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        
class ContactBook:
    def __init__(self):
        self._contacts =[]
        self._loadContacts()
    
    def Add(self,name,phone,email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
    
    def ShowAll(self):
        for c in self._contacts:
            self._PrintContact(c)
    
    def _PrintContact(self,contact):
        print('==========================================')
        print('Name: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('==========================================')

    def delete(self,name):
        for idx, c in enumerate(self._contacts):
            if name.lower() == c.name.lower():
                del self._contacts[idx]
                self._save()
                break
        else:#el else se ejecuta en caso de que no haya un break
            self._NotFound()

    def find(self,name):
        for c in self._contacts:
            if name.lower() == c.name.lower():
                self._PrintContact(c)
                break
        else:#el else se ejecuta en caso de que no haya un break
            self._NotFound()
    
    def update(self,name,newName,newPhone,newEmail):
        for idx, c in enumerate(self._contacts):
            if name.lower() == c.name.lower():
                self._contacts[idx].name = newName
                self._contacts[idx].phone = newPhone
                self._contacts[idx].email = newEmail
                self._save()
                break
        else:#el else se ejecuta en caso de que no haya un break
            self._NotFound()
    
    def _save(self):
        with open("contacts.csv","w") as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for c in self._contacts:
                writer.writerow((c.name,c.phone,c.email))
                
    def _loadContacts(self):
         with open("contacts.csv","r") as f:
            reader = csv.reader(f)
            for idx, c in enumerate(reader):
                if idx ==0:
                    continue
                self.Add(c[0],c[1],c[2])

    def _NotFound(self):
        print('!!!!!!!!!!!!!!!!!!!!!!!')
        print('   Contact not found   ')
        print('!!!!!!!!!!!!!!!!!!!!!!!')

def run():
    contactBook = ContactBook()

    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Name: '))
            phone = str(raw_input("Phone: "))
            email = str(raw_input("Email: "))
            contactBook.Add(name,phone,email)

        elif command == 'ac':
            name = str(raw_input('Name: '))
            newName = str(raw_input('New Name: '))
            newPhone = str(raw_input("New Phone: "))
            newEmail = str(raw_input("New Email: "))
            contactBook.update(name,newName,newPhone,newEmail)

        elif command == 'b':
            name = str(raw_input('Name: '))
            contactBook.find(name)

        elif command == 'e':
            name = str(raw_input('Name: '))
            contactBook.delete(name)

        elif command == 'l':
            contactBook.ShowAll()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')

if __name__ == '__main__':
    run()