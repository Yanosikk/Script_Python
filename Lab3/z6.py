import pickle
men_name_list = []
women_name_list = []
try:
    with open("imionazenskie.pkl", "rb") as women_binary_file:
        women_name_list = pickle.load(women_binary_file)
    with open("imionameskie.pkl", "rb") as men_binary_file:
        men_name_list = pickle.load(men_binary_file)
except FileNotFoundError:
    print("File has not been found")
while True:
    name = input("Insert your name or type koniec to stop: ")
    if name.lower() == "koniec":
        break
    
    if not name.isalpha():
        print("Name should contain only letters")
        continue
    name = name.capitalize()
    
    if name[-1] == 'a' and name not in ['Kosma', 'Barnaba', 'Bonawentura', 'Jarema', 'Kuba']:
        if name not in women_name_list:
            women_name_list.append(name)
        else:
            print("Name is already in the women's list.")
    elif name in ['Kosma', 'Barnaba', 'Bonawentura', 'Jarema', 'Kuba']:
        if name not in men_name_list:
            men_name_list.append(name)
        else:
            print("Name is already in the men's list.")
    else:
        if name not in men_name_list:
            men_name_list.append(name)
        else:
            print("Name is already in the men's list.")

women_name_list.sort()
men_name_list.sort()

print("Sorted women names: ", women_name_list)
print("Sorted men names: ", men_name_list)

with open("imionameskie.pkl", "wb") as men_binary_file:
    pickle.dump(men_name_list, men_binary_file)
    
with open("imionazenskie.pkl", "wb") as women_binary_file:
    pickle.dump(women_name_list, women_binary_file)

print("Sorted names has been appended to the .pkl file")
    
