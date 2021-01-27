# def fuction1(normal,*args,**kwargsbala):
#      print(normal)
#      for items in args:
#          print(items)
#      for key ,value in kwargsbala.items():
#          print(f"{key} is {value}")
# args=["Salil","shalaka","Chaitu","Arnav","Shivam\n"]
# normal= "There are few Good programmer Given Below :"
# kwargsbala={"Shalaka":"Doctor","Aai":"Teacher","Baba":"Clerk","Salil":"Programmer"}
# fuction1(normal,*args,**kwargsbala)


def function1(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}")
kwargs = {"A": "60","B": "40","C": "50","D": "80","E": "70"}
# function1(**kwargs)

print(kwargs.keys(),":",kwargs.values())
