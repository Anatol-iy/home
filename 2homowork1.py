def input_error(error_message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return error_message
            except TypeError:
                return error_message
            except IndexError:
                return error_message           
            except KeyError:
                return "Contact not found."
        return wrapper
    return decorator



class AddressBook:
    
    def __init__(self):    #Це конструктор класу. Викликається при створенні нового об'єкта класу 
        self.contacts = {} # пустой словарь для зберігання контактів. 

    @input_error("Give me name and phone please.")
    def add_contact(self, name, phone):
        self.contacts[name] = phone     # Додає новий запис до словника contacts, де ключ - це ім'я контакту,
        return "Contact added."         #а значення - номер телефону.

    @input_error("Give me name and phone, please.")
    def change_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone   #Якщо ім'я контакту існує, змінює номер телефону 
            return "Contact updated."          #для вказаного контакту на новий (new_phone).
        else:
            return "Contact not found."
    
    @input_error("Give me a valid name.")
    def show_phone(self, name):              #Якщо ім'я контакту існує, показывает номер телефона
        if name in self.contacts:
            return self.contacts[name]
        else:
            raise KeyError
    
    @input_error("Invalid command.")
    def show_all(self):                       #показывает все имена и телефоны
        if not self.contacts:
            return "No contacts available."
        else:
            return "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())
            #с новой строки присоединяет имя: телефон 

def parse_input(user_input):
    cmd, *args = user_input.split() #Перше слово визначається як команда (cmd), а решта слів стають списком аргументів (args).
    cmd = cmd.strip().lower()   #видаляє пробіли з початку і кінця і перетворює в ніжній регістр
    return cmd, args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:  #вечный цикл ввода команд пользователя
        user_input = input("Enter a command: ")
        if not user_input:    #Если пользователь ничего не ввел
            print("Please, enter your command.")
            continue 
        else:                 #если ввел, то обращаемся к функции def parse_input(user_input)
            command, args = parse_input(user_input)

        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            name, phone = args
            print(book.add_contact(name, phone)) #Цей блок коду викликає функцію add_contact об'єкта book

        elif command == "change":
            name, new_phone = args 
            print(book.change_contact(name, new_phone))#Цей блок коду викликає функцію change_contact об'єкта book

        elif command == "phone":
             if args:
                 name = args[0] #Якщо args не порожній, то name приймає значення першого елемента списку args
             else:
                 name = None  #Якщо args порожній, то name отримує значення None
             print(book.show_phone(name))# phone Jones", args буде ["Jones"], тому name буде встановлено на "Jones" 
                                         # і бот виводить номер телефону для контакту "Jones".
        elif command == "all":
            print(book.show_all())

        else:
            print("Invalid command.") #команда не є "good bye", "close", "exit", "hello", "add", "change", "phone", або "all", 
                                      #то виведеться повідомлення про невірну команду.

if __name__ == "__main__":   #виконується, коли файл викликається напряму (основна програма), 
    main()                   #а не імпортується як модуль в інший файл.