# ls = []
# for i in range(31):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(31) if i%3==0]
# print(ls)

# ------- ---------- ------------ -------------- ----------------- --------------

# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}

# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# ------- ---------- ------------ -------------- ----------------- --------------

# dresses = {dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]}
# print(type(dresses))
# print(dresses)

# ------- ---------- ------------ -------------- ----------------- --------------

# evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())

# for item in evens:
#     print(item)

# ------- ---------- ------------ -------------- ----------------- --------------

# ls = []
# ls = [i for i in range(12) if i%2==0]
# print(ls)

# ------- ---------- ------------ -------------- ----------------- --------------


Count = int(input("Enter the No. of items you want to add in the Dictionary. :\t "))
print("Enter the items you want to enter in the Dictionary. : \t")
L = {input() for i in range(Count)}
print(L)

# ------- ---------- ------------ -------------- ----------------- --------------

# while True:
#     print("you want...\n1.list comp\n2.dictionary comp\n3.set comp\n4.generator comp\n5.exit")
#     ch = int(input("1,2,3,4,5:"))
#     if ch is 1:
#         print("How many items to add:")
#         n = int(input())
#         print("Now add!!")
#         lst = [f"{input()}" for i in range(n)]
#         print(lst)
#
#     elif ch == 2:
#         print("Number of items to add:")
#         n = int(input())
#         print("Now add!!")
#         dict = {i: f"{input()}" for i in range(n)}
#         print(dict)
#
#     elif ch is 3:
#         print("How many items to add:")
#         n = int(input())
#         print("Now add!!")
#         sets = {f"{input()}" for i in range(n)}
#         print(sets)
#
#     elif ch is 4:
#         print("How many items to add:")
#         n = int(input())
#         gen = (f"{input()}" for i in range(n))
#         print(gen)
#
#     else:
#         print("Exiting...")
#
#
