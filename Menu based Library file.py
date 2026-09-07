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

    print("-" * 60)
    print("AccNo\tBookName\tBook Author\tNo. of Copies")
    print("-" * 60)

    for dec in F:
        st = dec.strip().split(",")

        print(f"{st[0]}\t{st[1]}\t\t{st[2]}\t\t{st[3]}")

    print("-" * 60)

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
