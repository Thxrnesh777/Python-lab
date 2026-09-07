def writee():
    f = open("e://emp.txt", "a")
    eid = int(input("Enter the Employee ID: "))
    ename = input("Enter the Employee Name: ")
    edesig = input("Enter the Employee Designation: ")
    esalary = int(input("Enter the Employee Salary: "))
    
    f.write(f"{eid},{ename},{edesig},{esalary}\n")
    f.close()

def readee():
    try:
        f = open("e://emp.txt", "r")
        print("-" * 60)
        print(f"{'Empid':<7} {'Employee name':<23} {'Employee Designation':<20} {'Salary':<10}")
        print("-" * 60)
        
        for rec in f:
            rt = rec.strip().split(",")
            if len(rt) == 4:
                print(f"{rt[0]:<7} {rt[1]:<23} {rt[2]:<20} {rt[3]:<10}")
        print("-" * 60)
        f.close()
    except FileNotFoundError:
        print("File not found! Please add record first.")


ch = 0
while ch != 3:
    print("\n1.write\n2.Read\n3.Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        writee()
    elif ch == 2:
        readee()
    elif ch == 3:
        pass
    else:
        print("Invalid Choice")

print("End of Program")
