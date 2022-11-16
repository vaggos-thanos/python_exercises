from operator import le


leksh = str(input("dose leksh: "))
counter1 = 0
counter2 = 0

while leksh.upper() != "ΤΕΛΟΣ":
    counter2 += 1
    if leksh.upper() == "ΔΟΜΗ":
        counter1 += 1

    leksh = str(input("dose leksh: "))

print( counter2 , "\n", counter1)