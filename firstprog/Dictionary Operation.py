Dict = {
    "salil":"MIT",
    "nikhil":"KKW",
    "ujjwal":"MBBS",
    "marks":[100,200,300]
}
def updateList(key,value):

    UpdateDict = {
        key : value
    }
    Dict.update(UpdateDict)
    print(Dict)

n = int(input("Enter 1 to Update\n\t  2 to Delete\n"))
if n is 1:
    i = int(input("How many keys & values u want to insert in Dictionary\t : "))
    for items in range(i):
        print("Enter the key & value for Dictionary \t :")
        key=input("Enter Key : ")
        value=input("Enter Value : ")
        updateList(key,value)
else:

    print("Before Deletion : \n",Dict.items())
    print("\n")
    key_want_to_delete = 'ujjwal'
    print("The Dictionary without "+ key_want_to_delete +" :")
    for keys,values in Dict.items():
        if keys is not key_want_to_delete:
            print(keys,values)
