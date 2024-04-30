name_list = []


for i in range(5):
    name = input("Insert your name: ")
    if not name.isalpha():
        print("Name should contain only letters")
        continue
    name = name.capitalize()
    
    if name in name_list:
        print(f"Name {name} is already in the list")
    else:
        name_list.append(name)
        print(f"The name {name} has been added to the list")

print("Names on the list: ", name_list)