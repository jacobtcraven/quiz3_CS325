while 2 > 1:
    begin = input("Would you like to start the program? (enter y or n): ")
    if begin == "no":
        continue
    if begin == "no":
        continue
    if begin == "yes":
        break
    elif begin == "y":
        break
    continue

while 2 > 1:
    fname = input("Please enter your first name: ")

    print(f"Your first name consists of {len(fname)} characters" )

    fnameback = ""

    for i in range(len(fname)):
        fnameback += fname[len(fname) - i - 1]

    print(f"Your first name spelled backwards is {fnameback}")

    lname = input("Enter your last name: ")

    print(f"Your last name consists of {len(lname)} characters. Thanks" )

    lnameback = ""

    for i in range(len(lname)):
        lnameback += lname[len(lname) - i - 1]

    print(f"Your first name backwards is {lnameback}")

    stop = input("Would you like to stop the program? (enter y or n)")
    if stop == "y":
        break
    else:
        continue
print("test")