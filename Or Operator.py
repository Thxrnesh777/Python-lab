A = int(input("Enter the value A:"))
R1= A % 8
R2= A % 4
if(R1==0 or R2==0):
    print ("A is Divisible by Both")

else:
    print("A is Not Divisible by Both")
