print("Welcome to python pizza 😎")

size_of_pizza = input("What size pizza do you want? s , m or l: ").lower()
add_extra_cheese = input("Do you want extra cheese? 'yes' or 'no'? ").lower()

bill = 0

if size_of_pizza == 's':
    bill += 15

elif size_of_pizza == 'm':
    bill += 20

elif size_of_pizza == 'l':
    bill += 25

if add_extra_cheese == 'yes':
    bill += 1

print(f"The total bill is ${bill}.")