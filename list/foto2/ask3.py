import random


list100 = []
for i in range(100):
    list100.append(random.randrange(-999, 999))

pos = []
neg = []

for number in list100:
    if number < 0:
        neg.append(number)
    elif number > 0:
        pos.append(number)

print(pos)
print(neg)