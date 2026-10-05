import sqlite3

con = sqlite3.connect("d://bank.db")
cur = con.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bank (
        accno INTEGER,
        name TEXT,
        acctype TEXT,
        balance INTEGER
    )
    """)
    con.commit()
    print("Table created successfully")


def insert_record():
    taccno = int(input("Enter Account Number: "))
    tname = input("Enter Account Holder Name: ")
    tacctype = input("Enter Account Type: ")
    tbalance = int(input("Enter Balance: "))

    cur.execute(
        "INSERT INTO bank VALUES(?, ?, ?, ?)",
        (taccno, tname, tacctype, tbalance)
    )

    con.commit()
    print("Record inserted successfully")


def update_record():
    taccno = int(input("Enter Account Number to update: "))
    tbalance = int(input("Enter new Balance: "))

    cur.execute(
        "UPDATE bank SET balance=? WHERE accno=?",
        (tbalance, taccno)
    )

    con.commit()
    print("Record updated successfully")


def delete_record():
    taccno = int(input("Enter Account Number to delete: "))

    cur.execute(
        "DELETE FROM bank WHERE accno=?",
        (taccno,)
    )

    con.commit()
    print("Record deleted successfully")


def select_records():
    cur.execute("SELECT * FROM bank")
    records = cur.fetchall()
    
    print("_" * 80)
    print(f"\n{'Acc No':<20}{'Name':<20}{'Acc Type':<20}{'Balance':>20}")
    print("_" * 80)

    for record in records:
        print(f"{record[0]:<20}{record[1]:<20}{record[2]:<20}{record[3]:>20}")

    print("_" * 80)



while True:
    print("\n===== BANK DATABASE =====")
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
