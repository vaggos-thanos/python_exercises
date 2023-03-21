File = open('pth.txt', 'r')

pol = []
therm = []
i = 0
for line in File:
    if i % 2 == 1:
        pol.append(line)
    else:
        therm.append(float(line))
    i += 1

print(pol)
print(therm)
File.close()