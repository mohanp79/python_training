import copy
a = {1: [1,2,3]}
b = a.copy()
print("Shallo Copy:",a,b)
a[1].append(4)
print("After append Shallo Copy:",a,b)

c = copy.deepcopy(a)

print("Deep Copy:",a,c)

a[1].append(5)

print("After append Deep Copy:",a,c)
