def library_write():
    F = open("e://library.txt", "a")

    accno = int(input("Enter the AccNo: "))
    book_name = input("Enter the Book name: ")
    book_auth = input("Enter the Book Author: ")
    no_copies = int(input("Enter the No. of Copies: "))

    F.write(f"{accno},{book_name},{book_auth},{no_copies}\n")
    F.close()


def library_read():
    F = open("e://library.txt", "r")

    print("-" * 75)
    print(f"{'AccNo':<15}{'BookName':<20}{'Book Author':<20}{'No. of Copies':<15}")
    print("-" * 75)

    for dec in F:
        st = dec.strip().split(",")

        print(f"{st[0]:<15}{st[1]:<20}{st[2]:<20}{st[3]:<15}")

    print("-" * 75)

    F.close()

Ch = 0

while Ch != 3:

    print("\n1.Write")
    print("2.Read")
    print("3.Exit")

    Ch = int(input("Enter your choice: "))

    if Ch == 1:
        library_write()

    elif Ch == 2:
        library_read()

    elif Ch == 3:
        print("End of Program")

    else:
        print("Invalid Choice")
