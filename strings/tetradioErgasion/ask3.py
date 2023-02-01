total = 0
string = input("give word: ")
while string[-1] != "Ω" and string[-1] != "ω":
    if string[0] == "Α" or string[0] == "α":
        total += 1
    string = input("give word: ")
    
print(total)