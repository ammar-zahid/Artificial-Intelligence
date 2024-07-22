basket = (1,2,4,1,2,5,6,7,3,1)

print(type(basket))

print(basket.count(2))

print(basket.index(4))

#we can use multiple methods with tuples

#concatenate
tup1 = (1,2,8)
tup2 = (4,5,6)
add = tup1 + tup2
print(add)

#repetition
rep = tup1 * 3
print(rep)

#membership (in keyword)
mem = (9 in basket)
print(mem)

#len
#min and max
print(min(basket))
print(max(basket))

#slicing
sliced = basket[2:5]
print(sliced)

#unpacking
a, b, c = tup1
print(a,c)