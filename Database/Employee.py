import sqlite3

con = sqlite3.connect("e://employee.db")
cur = con.cursor()

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        eid INTEGER,
        ename TEXT,
        edesign TEXT,
        esalary INTEGER
    )
    """)
    con.commit()
    print("Table created successfully")


def insert_record():
    teid = int(input("Enter Employee ID: "))
    tename = input("Enter Employee Name: ")
    tdesign = input("Enter Employee Designation: ")
    tesalary = int(input("Enter Employee Salary: "))

    cur.execute(
        "INSERT INTO employee VALUES(?, ?, ?, ?)",
        (teid, tename, tdesign, tesalary)
    )

    con.commit()
    print("Record inserted successfully")


def update_record():
    teid = int(input("Enter Employee ID to update: "))
    tesalary = int(input("Enter new Salary: "))

    cur.execute(
        "UPDATE employee SET esalary=? WHERE eid=?",
        (tesalary, teid)
    )

    con.commit()
    print("Record updated successfully")


def delete_record():
    teid = int(input("Enter Employee ID to delete: "))

    cur.execute(
        "DELETE FROM employee WHERE eid=?",
        (teid,)
    )

    con.commit()
    print("Record deleted successfully")


def select_records():
    cur.execute("SELECT * FROM employee")
    records = cur.fetchall()

    print(f"\n{'EID':<10}{'Name':<20}{'Designation':<20}{'Salary':<10}")
    print("-" * 60)

    for record in records:
        print(f"{record[0]:<10}{record[1]:<20}{record[2]:<20}{record[3]:<10}")


# Menu
while True:
    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Create Table")
    print("2. Insert")
    print("3. Update")
    print("4. Delete")
    print("5. Select")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_table()
    elif choice == 2:
        insert_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        select_records()
    elif choice == 6:
        break
    else:
        print("Invalid choice")

con.close()
print("Program terminated")
