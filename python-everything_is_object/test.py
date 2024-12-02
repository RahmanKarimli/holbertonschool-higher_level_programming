

a = [1,2,3]
b = a
a = a + [4]

print(a)
print(b)
print(id(a)==id(b))
print(a is b)
print(a == b)


print("------")
x = [1,2,3]
print(id(x))
# x.append(4)
x += [4]
print(id(x))


print("-----")
def inc(n):
    n.append(3)
a = [1,2]
inc(a)
print(a)


print("-------")
a = ("a")
print(type(a))









