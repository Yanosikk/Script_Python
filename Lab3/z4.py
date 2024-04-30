name_list = []

try:
    with open("imiona.txt", "r") as file:
        for lane in file:
            name = lane.strip()
            name_list.append(name)
except FileNotFoundError:
    print("File does not exist")


while True:
    name = input("Insert your name or type koniec to stop: ")
    if name.lower() == "koniec":
        break
    
    if not name.isalpha():
        print("Name should contain only letters")
        continue
    name = name.capitalize()
    
    if name in name_list:
        print(f"Name {name} is already in the list")
    else:
        name_list.append(name)
        print(f"The name {name} has been added to the list")

name_list.sort()
with open("imiona.txt", "w") as file:
    for name in name_list:
        file.write(name + "\n")

print("Sorted names has been appended to the list")
    