dics1 = { "Set":"Collection of the Object of Same Thing",
       "Subset":"Subset is the part of the set ",
       "Union":"sumation of all the element inside the Set",
       "intersetion":"Difference element of Two different set OR Odd Element Out "
          }
# Update the dicstonary !
dics1["Fruits:"]="Mango","Apple","Banana"
dics1["Salil"]="Today i'm going to eat yummy home made icecream"
print(dics1)
dics1.update({"Salil":"Coffe"})
print(dics1)

print(dics1.get("Set"))
print(dics1.get("Subset"))
print(dics1.get("Union"))
print(dics1.get("intersetion"))
print(dics1.get(("Fruits")))
print(dics1.get("Salil"))

# To Show Keys & items
print(dics1.keys())
print(dics1.items())

