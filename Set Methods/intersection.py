a = set()
n1 = int(input("Enter number of elements in first set: "))
for i in range(n1):
    x = int(input())
    a.add(x)

b = set()
n2 = int(input("Enter number of elements in second set: "))
for i in range(n2):
    x = int(input())
    b.add(x)

print(a.intersection(b))
