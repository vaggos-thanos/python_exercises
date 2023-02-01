array = []
num = float(input("give number: "))
while num != 0:
    array.append(num)
    num = float(input("give number: "))

number = []
for i in range(len(array)):
    number.append(array.pop())

print(number)