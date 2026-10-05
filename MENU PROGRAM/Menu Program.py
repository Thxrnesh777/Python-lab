print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

ch=int(input("Enter the Choice:"))

if(ch==1):
    A=int(input("Enter the value: "))
    B=int(input("Enter the value: "))
    C= A+B
    print("Answer:", C)

elif(ch==2):
    A=int(input("Enter the value: "))
    B=int(input("Enter the value: "))
    C= A-B
    print("Answer:", C)

elif(ch==3):
    A=int(input("Enter the value: "))
    B=int(input("Enter the value: "))
    C= A*B
    print("Answer:", C)

elif(ch==4):
    A=int(input("Enter the value: "))
    B=int(input("Enter the value: "))
    C= A/B
    print("Answer:", C)

else:
    print("Invalid Choice")    
