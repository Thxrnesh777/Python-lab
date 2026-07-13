A =[]
B =[]
C =[]

for i in range(0,5):
    X = int (input("Enter Number for A: "))
    A.append(X)

for i in range(0,5):
    X = int (input("Enter Number for B: "))
    B.append(X)

for i in range(0,5):
    Result = A[i]+B[i]
    C.append(Result)

print("\n A:",A)
print("\n B:",B)
print("\n C:",C)

