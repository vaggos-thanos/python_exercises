min = 10**9
max = 10**-9
for i in range(10):
    number = input("dose arithmo")
    if number > max:
        max = number
    if number < min:
        min = number
    
print max , min
