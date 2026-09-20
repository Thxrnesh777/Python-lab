import sqlite3

con = sqlite3.connect("e://student.db")
cur = con.cursor()

def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stud (
        rno INTEGER,
        name TEXT,
        addr TEXT,
        mark1 INTEGER
    )
    """)
    con.commit()
    print("Table created successfully")


def insert_record():
    trno = int(input("Enter Roll No: "))
    tname = input("Enter Name: ")
    taddr = input("Enter Address: ")
    tmark1 = int(input("Enter Mark 1: "))

    cur.execute(
        "INSERT INTO stud VALUES(?, ?, ?, ?)",
        (trno, tname, taddr, tmark1)
    )

    con.commit()
    print("Record inserted successfully")


def update_record():
    trno = int(input("Enter Roll No to update: "))
    tmark1 = int(input("Enter new Mark 1: "))

    cur.execute(
        "UPDATE stud SET mark1=? WHERE rno=?",
        (tmark1, trno)
    )

    con.commit()
    print("Record updated successfully")


def delete_record():
    trno = int(input("Enter Roll No to delete: "))

    cur.execute(
        "DELETE FROM stud WHERE rno=?",
        (trno,)
    )

    con.commit()
    print("Record deleted successfully")


def select_records():
    cur.execute("SELECT * FROM stud")
    records = cur.fetchall()

    print(f"\n{'Rno':<10}{'Name':<20}{'Address':<20}{'Mark1':<10}")
    print("-" * 60)

    for record in records:
        print(f"{record[0]:<10}{record[1]:<20}{record[2]:<20}{record[3]:<10}")


# Menu
while True:
    print("\n===== STUDENT DATABASE =====")
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
