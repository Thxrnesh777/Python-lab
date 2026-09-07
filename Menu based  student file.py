def writeacc():
    f = open("e://student.txt", "a")
    rno = int(input("Enter the student Roll No.: "))
    name = input("Enter the student Name: ")
    address = input("Enter the student Address: ")
    mark1 = int(input("Enter the student mark1: "))

    f.write(f"{rno},{name},{address},{mark1}\n")
    f.close()


def readrec():
    f = open("e://student.txt", "r")

    print("-" * 60)
    print(f"{'Rno':<10}{'Name':<20}{'Address':<20}{'Mark1':<10}")
    print("-" * 60)

    for rec in f:
        st = rec.strip().split(",")
        print(f"{st[0]:<10}{st[1]:<20}{st[2]:<20}{st[3]:<10}")

    print("-" * 60)
    f.close()


ch = 0

while ch != 3:
    print("\n1.Write\n2.Read\n3.Exit")
    ch = int(input("Enter your choice: "))

    print("Write") if ch == 1 else print("Read") if ch == 2 else print("Exit") if ch == 3 else print("Invalid choice")

    if ch == 1:
        writeacc()
    elif ch == 2:
        readrec()

print("End of program")
