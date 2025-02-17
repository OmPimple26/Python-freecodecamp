set1={"Roger","Syd","Roger"}
set2={"Roger"}

intersect=set1 & set2
print(intersect)

mod=set1 | set2
print(mod)

diff=set1 - set2
print(diff)

#Subset
subset=set1<set2
print(subset)

subset=set1>set2
print(subset)

print(list(set1))