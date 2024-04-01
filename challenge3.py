# Hey todays we are making true love counter.
#so ,let's start..

print("The love calculeter is calculating your score...")

name1 = input("Enter your partner name:")
name2 = input("Enter yoursecond partner name:")

Combined_name = name1 + name2
lover_names = Combined_name.lower()

t=lover_names.count("t")
r=lover_names.count("r")
u=lover_names.count("u")
e=lover_names.count("e")

first_digit = t+r+u+e

l=lover_names.count("l")
o=lover_names.count("o")
v=lover_names.count("v")
e=lover_names.count("e")

second_digit = l+o+v+e
total_digit =int(str(first_digit) + str(second_digit))

if (total_digit < 10) or (total_digit > 90):
    print(f"your score is {total_digit},you go together like coke and mentos.")
elif (total_digit >= 40) and (total_digit <=50):
    print(f"your score is {total_digit},you are alright toghther")
else:
    print(f"your score is {total_digit}")