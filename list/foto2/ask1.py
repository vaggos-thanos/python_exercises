total_sum = 0
numbers = []
number = int(input("give a number"))
while total_sum <= 1000:
    total_sum += number
    numbers.append(number)
    number = int(input("give a number"))

print(total_sum)
print(total_sum / len(numbers))
max_num=0
for i in range(len(numbers)):
    if i == 0:
        max_num = numbers[i]
    if numbers[i] > max_num:
        max_num = numbers[i]  

counter=0
for number in numbers:
    if max_num == number:
        counter+=1

print(max_num)
print(counter)