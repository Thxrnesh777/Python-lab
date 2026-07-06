A = int(input("Enter the value A: "))
B = int(input("Enter the value B: "))
C = int(input("Enter the value C: "))
D = int(input("Enter the value D: ")) 

if (A > B) and (A > C) and (A > D):
    print("A is Greater")

elif (B > C) and (B > D):
    print("B is Greater")

elif (C > D):
    print("C is Greater")

else:
    print("D is Greater")
