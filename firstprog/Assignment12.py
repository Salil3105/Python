f = open("Assignment12", "rt")
# print(f.read())

word = input("Enter the word u want to search ?\n")
s = " "
count = 1
while(s):
    s = f.readline()
    L = s.split()
    if word in L:
        print("Line No." ,count ,":" , s)
    else:
        print("Sorry, Word is not found !\n")
    count+=1

f.close()
