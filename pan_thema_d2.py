File = open('pth.txt', 'r')
file = File.read()
File.close()
file = file.split("\n")

pol = []
therm = []

for i in range(len(file)):
    if i % 2 == 0:
        pol.append(file[i])
    else:
        therm.append(file[i])

print(pol)
print(therm)