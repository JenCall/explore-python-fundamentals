# Variables
# Explore the Problem with Immutable vs. Mutable Objects

# integer -> immutable
a = 8
b = a
b = 5
print(a,b)
print(id(a))
print(id(b))

# float -> immutable
c = 9.5
d = c
d = 10.5
print(c,d)
print(id(c))
print(id(d))

# str -> immutable
f = "Hello"
g = f
g = "World"
print(f,g)
print(id(f))
print(id(g))

# list -> mutable
h = [1,2,3]
i = h
i[0] = 4
print(h,i)
print(id(h))
print(id(i)) # same id as h

# tuple -> immutable by design
j = ("apple", "banana", "cherry")
k = j
k[0] = "kiwi"
print(j,k)

# dict -> mutable
l = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
m = l
m["brand"] = {"tesla"}
print(l,m)
print(id(l))
print(id(m))
# l and m share same ids
