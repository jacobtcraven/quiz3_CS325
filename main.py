fname = input("Please enter your first name: ")

print(f"Your first name consists of {len(fname)} characters" )

fnameback = ""

for i in range(len(fname)):
    fnameback += fname[len(fname) - i - 1]

print(f"Your first name backwards is {fnameback}")