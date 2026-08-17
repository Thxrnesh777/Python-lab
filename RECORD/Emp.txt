f1 = open("e://BCA//Emp.txt", "w")

for i in range(0, 10):

    empid = int(input("Enter Empid: "))
    empname = input("Enter Empname: ")
    designation = input("Enter Designation: ")
    department = input("Enter Department: ")
    address = input("Enter Address: ")
    salary = int(input("Enter Salary: "))

    f1.write(str(empid) + " " + empname + " " + designation + " " +
             department + " " + address + " " + str(salary) + "\n")

f1.close()

f1 = open("e://BCA//Emp.txt", "r")

record = f1.read()

print("Employee Records are:\n")
print(record)

f1.close()
