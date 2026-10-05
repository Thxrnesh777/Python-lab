import sqlite3

con = sqlite3.connect("d://flight.db")
cur = con.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS flight (
        flightid INTEGER,
        source TEXT,
        destination TEXT,
        fare INTEGER
    )
    """)
    con.commit()
    print("Table created successfully")


def insert_record():
    tfid = int(input("Enter Flight ID: "))
    tsource = input("Enter Source: ")
    tdestination = input("Enter Destination: ")
    tfare = int(input("Enter Fare: "))

    cur.execute(
        "INSERT INTO flight VALUES(?, ?, ?, ?)",
        (tfid, tsource, tdestination, tfare)
    )

    con.commit()
    print("Record inserted successfully")


def update_record():
    tfid = int(input("Enter Flight ID to update: "))
    tfare = int(input("Enter new Fare: "))

    cur.execute(
        "UPDATE flight SET fare=? WHERE flightid=?",
        (tfare, tfid)
    )

    con.commit()
    print("Record updated successfully")


def delete_record():
    tfid = int(input("Enter Flight ID to delete: "))

    cur.execute(
        "DELETE FROM flight WHERE flightid=?",
        (tfid,)
    )

    con.commit()
    print("Record deleted successfully")


def select_records():
    cur.execute("SELECT * FROM flight")
    records = cur.fetchall()

    print("_" * 80)
    print(f"{'Flight ID':<20}{'Source':<20}{'Destination':<20}{'Fare':>20}")
    print("_" * 80)

    for record in records:
        print(f"{record[0]:<20}{record[1]:<20}{record[2]:<20}{record[3]:>20}")

    print("_" * 80)


while True:
    print("\n===== FLIGHT DATABASE =====")
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
