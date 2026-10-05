def flight_write():
    F = open("d://Flight.txt", "a")

    flight_id = int(input("Enter the Flight ID: "))
    source = input("Enter the Source: ")
    destination = input("Enter the Destination: ")
    fare = float(input("Enter the Fare Amount: "))

    F.write(f"{flight_id},{source},{destination},{fare}\n")
    F.close()


def flight_read():
    try:
        F = open("d://Flight.txt", "r")

        print("_" * 80)
        print(f"{'Flight ID':<15}{'Source':<20}{'Destination':<20}{'Fare':>15}")
        print("_" * 80)

        for dec in F:
            st = dec.strip().split(",")

            print(f"{st[0]:<15}{st[1]:<20}{st[2]:<20}{st[3]:>15}")

        print("_" * 80)
        F.close()

    except FileNotFoundError:
        print("Flight file not found!")


Ch = 0

while Ch != 3:

    print("\n1.Write")
    print("2.Read")
    print("3.Exit")

    Ch = int(input("Enter your choice: "))

    if Ch == 1:
        flight_write()

    elif Ch == 2:
        flight_read()

    elif Ch == 3:
        print("End of Program")

    else:
        print("Invalid Choice")
