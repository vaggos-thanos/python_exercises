a = [2,1,3,2,1,3,2,1,1,2,3,2,1,3,1,2,3,1]

one = 0
two = 0
three = 0

for i in range(len(a)):
    if a[i] == 1:
        one += 1
    elif a[i] == 2:
        two += 1
    elif a[i] == 3:
        three += 1

for i in range(one + two + three):
    if i <= one:
        a[i] = 1
    elif i <= one + two:
        a[i] = 2
    else:
        a[i] = 3

print(a)