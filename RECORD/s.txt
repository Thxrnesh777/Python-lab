f1 = open("e://BCA//s.txt", "w")

for i in range(0, 10):

    rno = int(input("Enter RegNo: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    f1.write(str(rno) + " " + name + " " + str(marks) + "\n")

f1.close()

f1 = open("e://BCA//s.txt", "r")

record = f1.read()

print("Record is:")
print(record)

f1.close()
