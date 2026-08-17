f1 = open("E://BCA//Lib.txt", "w")

for i in range(0, 10):

    accno = int(input("Enter Accno:"))
    bookname = input("Enter Bookname:")
    author = input("Enter Author:")
    publisher = input("Enter Publisher:")
    noofcopies = int(input("Enter Noofcopies: "))

    f1.write(str(accno) + " " + bookname + " " + author + " " +
             publisher + " " + str(noofcopies) + "\n")

f1.close()

f1 = open("E://BCA//Lib.txt", "r")

record = f1.read()

print("Library Records are:\n")
print(record)

f1.close()
