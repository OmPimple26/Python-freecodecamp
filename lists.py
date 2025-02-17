dogs=["Roger",1,"Syd",True,"Quincy",7]

print(dogs)

print("Beau" in dogs)

print(dogs[2])

dogs[2]="Moti"
print(dogs)

print(dogs[2:4])

print(dogs[2:])

print(dogs[:3])

print(len(dogs))

dogs.append("Judah")

dogs.extend(["Judah","Beau"])

dogs+=["Sheru",5]

dogs.remove("Quincy")
print(dogs)

print(dogs.pop())
print(dogs)

items=["Roger",1,"Syd",True,"Quincy",7]
items[1:1]=["Test1","Test2"]
print(items)


# Sorting in python
items=["Roger","Syd","Quincy","Beau"]
items.sort()
print(items)

items=["Roger","bob","Quincy","Bob"]
items.sort(key=str.lower)
print(items)

itemscopy=items[:]
print(itemscopy)

print(sorted(items,key=str.lower))