# s = set() # empty set

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
# print(len(s))
# print(type(s))
# s.add(10)
# s.remove(2)
# print(s)

print(s1.union(s2))
print(s1.intersection(s2))

print(s1-s2) #returns s1 only , not the common value of s1 and s2
print(s2-s1) #returns s2 only , not the common value of s1 and s2