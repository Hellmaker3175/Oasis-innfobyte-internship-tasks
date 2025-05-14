import random
import string

length = int(input("Enter the length of the password you want to generate: "))

print("\nChoose the option from the list below:")
print("1. Numbers")
print("2. Letters")
print("3. Symbols")
print("4. Numbers + Letters")
print("5. Letters + Symbols")
print("6. Numbers + Symbols")
print("7. All categories")

option = int(input("Enter your choice (1-7): "))

numbers = string.digits            
letters = string.ascii_letters     
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

categories = ""

if option == 1:
    categories = numbers
elif option == 2:
    categories = letters
elif option == 3:
    categories = symbols
elif option == 4:
    categories = numbers + letters
elif option == 5:
    categories = letters + symbols
elif option == 6:
    categories = numbers + symbols
elif option == 7:
    categories = numbers + letters + symbols
else:
    print("Invalid option. Please run the program again.")
    exit()

password = ''.join(random.choices(categories, k=length))
print("\nGenerated Password:", password)


