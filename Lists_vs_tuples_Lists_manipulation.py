#tuple is immutable where as List is mutable(can be changed)

# tuples are mainly used for variables asignment tuples use (), lists use []

def example():
    return 15,20

a,b = example()

print(a)
print(b)

x = [4,6,3,8,7]

print(x, x[2])

x.append(13)

print(x)

x.insert(2,21)

print(x)

x.remove(3) # removes first element if there are multiple 3's

print(x)

print(x.count(3))

x.sort()
print(x)
