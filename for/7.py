count  = 0
sum = 0
for i in range(10):
    vathmos = input("dose vathmo mathiti: ")
    sum += vathmos
    if vathmos < 100:
        count += 1
pososto = (count / 10.0) * 100
print pososto
