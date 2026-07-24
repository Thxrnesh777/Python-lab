a = set()
n1 = int(input("Enter number of elements in first set: "))
for i in range(n1):
    a.add(int(input()))

b = set()
n2 = int(input("Enter number of elements in second set: "))
for i in range(n2):
    b.add(int(input()))

print(a.issubset(b))
