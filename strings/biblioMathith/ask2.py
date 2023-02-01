count = 0
word = raw_input("dose leksi")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in word:
    if char in letters:
        count +=1

print count
    
    