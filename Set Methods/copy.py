a = set()
n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input())
    a.add(x)

b = a.copy()

print(b)
