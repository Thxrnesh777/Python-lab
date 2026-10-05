
def bank_write():
    F = open("d://BANK.txt", "a")

    accno = int(input("Enter the Account No: "))
    name = input("Enter the Account Holder Name: ")
    acc_type = input("Enter the Account Type (Saving/Current): ")
    balance = float(input("Enter the Balance: "))

    F.write(f"{accno},{name},{acc_type},{balance}\n")
    F.close()


def bank_read():
    try:
        F = open("d://BANK.txt", "r")

        print("_" * 80)
        print(f"{'AccNo':<20}{'Name':<20}{'AccType':<20}{'Balance':>20}")
        print("_" * 80)

        for dec in F:
            st = dec.strip().split(",")

            print(f"{st[0]:<20}{st[1]:<20}{st[2]:<20}{st[3]:>20}")

        print("_" * 80)
        F.close()

    except FileNotFoundError:
        print("Bank file not found!")


Ch = 0

while Ch != 3:
    print("\n1.Write")
    print("2.Read")
    print("3.Exit")

    Ch = int(input("Enter your choice: "))

    if Ch == 1:
        bank_write()

    elif Ch == 2:
        bank_read()

    elif Ch == 3:
        print("End of Program")

    else:
        print("Invalid Choice")
