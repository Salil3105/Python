# print("WELCOME")
#
# while True:
#     i = int(input("Enter a number"))
#     if i>=100:
#         print(i)
#         print("Got a value greater than 100")
#         break
#     else:
#         continue

# -------------------Break , Continue & Pass--------------------

# Python program to demonstrate
# break, continue and pass

s = 'geeksforgeeks'

for letter in s:
    if letter == 'e' or letter == 's':
        break
    print(letter, end=" ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print(letter, end=" ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        pass
    print(letter, end=" ")
