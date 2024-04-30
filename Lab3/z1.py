dictionary = {"0" : "Zero", "1" : "Jeden", "2" : "Dwa", "3" : "Trzy", "4" : "Cztery", "5" : "Pięć", "6" : "Sześć", "7" : "Siedem", "8" : "Osiem", "9" : "Dziewięć"}

def exchange_to_words(number):
    return dictionary.get(number, "Value_Error")

number = input("Insert number from 0 to 9: ")

result = exchange_to_words(number)
print(f"{number} is {result}")