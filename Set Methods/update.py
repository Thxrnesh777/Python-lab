s = {1, 2}
x = input("Enter elements separated by space: ")
s.update(map(int, x.split()))
print(s)
