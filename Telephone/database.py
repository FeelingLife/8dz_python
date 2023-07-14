def write_name(name):
    with open("telephone.txt","a",encoding="UTF-8") as file:
        file.write(name)

def search_data(char):
    count = 0
    find_man = []
    with open("telephone.txt","r",encoding="UTF-8") as file:
        man = file.readlines()
        for row in man:
            if char in row:
                count += 1
                print(f"{count}) {row.strip()}")
                find_man.append(row)

    return find_man

def change_data(old_data, new_data):
    with open("telephone.txt","r",encoding="UTF-8") as file:
        data = file.readlines()
    with open("telephone.txt","w",encoding="UTF-8") as file:
        for row in data:
            if row == old_data:
                file.write(new_data)
            else:
                file.write(row)

def delete_data(old_data):
    with open("telephone.txt","r",encoding="UTF-8") as file:
        data = file.readlines()
    with open("telephone.txt","w",encoding="UTF-8") as file:
        for row in data:
            if row == old_data:
                file.write(row)
            else:
                file.write(row)