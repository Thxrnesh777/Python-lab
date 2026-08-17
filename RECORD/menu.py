print("1. Read")
print("2. Write")
print("3. Append")

ch = int(input("Enter the Choice: "))

if ch == 1:
    f1 = open("e://BCA//s.txt", "r")

    record = f1.read()

    print("Record is:")
    print(record)

    f1.close()

elif ch == 2:
    f1 = open("e://BCA//s.txt", "w")

    for i in range(0,11):
        rno = int(input("Enter RegNo: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        f1.write(str(rno) + " " + name + " " + str(marks) + "\n")

    f1.close()


elif ch == 3:
    f1 = open("e://BCA//s.txt", "a")

    for i in range(0, 11):
        rno = int(input("Enter RegNo: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        f1.write(str(rno) + " " + name + " " + str(marks) + "\n")

    f1.close()


else:
    print("Invalid Choice")
