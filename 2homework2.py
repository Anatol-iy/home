from collections import UserDict
class Field:                     #базовий клас для полів
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):            #зберігає імя 
    def __init__(self, value):
        super().__init__(value)
    def __str__(self):
        return "Name:" + super().__str__()

class Phone(Field):
     def __init__(self, value):
        super().__init__(value)
        
        if not value.isdigit() or len(value) != 10:  # Валідація номера телефону (має бути 10 цифр)
            raise ValueError("Invalid phone number")

class Record:                        #зберігання інформації про контакт
    def __init__(self, name):
        self.name = Name(name)       #зберігання об'єкта Name в окремому атрибуті.
        self.phones = []             # зберігання списку об'єктів Phone в окремому атрибуті.
    
    def add_phone(self, phone_number):
        phone = Phone(phone_number)  #экземпляр класса Phone c номером телефона
        self.phones.append(phone)    

    def remove_phone(self, phone_number): #удаление
        for phone in self.phones[:]:  
            if phone.value == phone_number:
                self.phones.remove(phone)


    def edit_phone(self, old_number, new_number): #редагування
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                break

    def find_phone(self, phone_number): #найти номер
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):    #зберігання та управління записами 
   
    def add_record(self, contact):
        self.data[contact.name.value] = contact  # Зберігаємо об'єкт класу Record, а не словник
        print(f"Your contact {contact.name} has been added to AddressBook")

    def find(self, name):
        if name in self.data:
            return self.data[name] 
        else:
            print('This contact is absent in Addressbook')

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f'Contact {name} has been removed in AddressBook')



#john_record = Record("John")# Створення запису
#john_record.add_phone("1234567890")
#john_record.add_phone("5555555555")
#print(john_record)
book = AddressBook()



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Знаходження запису John
john = book.find("John")

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("5555555555", "1112223333")

print(found_phone)