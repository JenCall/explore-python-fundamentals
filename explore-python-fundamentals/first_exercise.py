# Variables
# Explore the Problem with Immutable vs. Mutable Objects

# integer -> immutable
a = 8
b = a
b = 5
print(a,b)

# float -> immutable
c = 9.5
d = c
d = 10.5
print(c,d)

# str -> immutable
f = "Hello"
g = f
g = "World"
print(f,g)

# list
h = [1,2,3]
i = h
i[0] = 4
print(h,i)

# tuple
j = ("apple", "banana", "cherry")
k = j
k[0] = "kiwi"
print(j,k)

# dict
l = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

m = l
m[0] = {"hello":"world"}
print(l,m)
