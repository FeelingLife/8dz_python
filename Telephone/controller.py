from database import*
from view import*

def main():
    while True:
        num = input_num()
        if num == 1:
            name = input_name()
            write_name(name)
            print("Успешно записано \n")
        elif num == 2:
            char = input_search()
            search_data(char)
            print("Успешно найдено \n")
        elif num == 3:
            char = input_search()
            find_man = search_data(char)
            select_num = select_number()
            new_man = input_name()
            change_data(find_man[select_num-1],new_man)
            print("Успешно переименовано \n")
        elif num == 4:
            char = input_search()
            find_man = search_data(char)
            select_num = select_number()
            delete_data(find_man[select_num-1])
            print("Успешно удалено \n")
        elif num == 5:
            print("Выход")
            return()

main()
