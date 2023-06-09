from datetime import datetime


def main():
    count = 1
    current_datetime = datetime.now()
    while True:
        print("Меню заметок:\n"
              "Посмотреть все заметки, нажмите: 1\n"
              "Добавить новую заметку, нажмите: 2\n"
              "Редактировать заметку, нажмите: 3\n"
              "Удалить заметку: 4\n")
        number_choice = int(input("Введите номер: "))
        if number_choice == 2:
            print(f"Введите данные для заметки № {count} ")
            with open('notes.txt', 'a', encoding='utf-8') as file:
                file.write(f"{count}; ")
                header = input("Введите заголовок для новой заметки: ")
                file.write(f"{header}; ")
                body_header = input("Введите текст заметки: ")
                file.write(f"{body_header}; ")
                file.write(f"day-{current_datetime.day}; time-{current_datetime.hour}:{current_datetime.minute}\n")
            count += 1

        elif number_choice == 1:
            with open('notes.txt', 'r', encoding='utf-8') as file:
                data_1 = file.readlines()
                print("\nДанные в таблице:\n")
                for elem in data_1:
                    new_elem = elem.replace(";", "  ")
                    print(new_elem)

        elif number_choice == 4:
            number_header_del = input("Введите номер заголовка(удалить): ")
            with open('notes.txt', 'r', encoding='utf-8') as file:
                data_4 = file.readlines()
            for i in data_4:
                if i[0] == number_header_del:
                    print(f"Заголовок номер {number_header_del} удалён\n")
                    data_4.remove(i)
                    with open("notes.txt", "w") as file:
                        file.writelines(data_4)

        elif number_choice == 3:
            number_header_edit = input("Введите номер заголовка цифрой: ")
            new_header_edit = input("Введите новый заголовок(для редакции): ")
            new_body_edit = input("Введите тело заголовка(для редакции): ")
            with open('notes.txt', 'r', encoding='utf-8') as file:
                data_3 = file.readlines()
            new_str = ""
            for i in data_3:
                if i[0] == number_header_edit:
                    new_str += f"{i[0]}; {new_header_edit}; {new_body_edit}; "
                    new_str += f"day-{current_datetime.day}; time-{current_datetime.hour}:{current_datetime.minute}\n"

            data_3[int(number_header_edit)] = new_str
            with open('notes.txt', 'w', encoding='utf-8') as file:
                file.writelines(data_3)

        else:
            print("Неверный ввод, повторите попытку\n")

























if __name__ == '__main__':
    main()
