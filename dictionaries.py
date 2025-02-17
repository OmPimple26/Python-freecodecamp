dog={"name":"Roger","age":8,"color":"green"}
print(dog.get("color","brown"))

print(dog.pop("name"))
print(dog)

print(dog.popitem())
print(dog)

print("color" in dog)

print(dog.keys())

print(list(dog.keys()))

print(dog.values())

print(list(dog.values()))

print(list(dog.items()))

print(len(dog))

dog["favourite food"]="Meat"
print(dog)

del dog['color']
print(dog)

dogCopy=dog.copy()