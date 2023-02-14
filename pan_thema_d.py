KOD = []
VATH = []

code = str(input("Δώσε κωδικό: "))
while code != "ΤΕΛΟΣ":
    KOD.append(code)
    grade = int(input("Δώσε βαθμό: "))
    while grade not in range(1, 101):
        grade = int(input("Δώσε βαθμό: "))
    VATH.append(grade)
    code = str(input("Δώσε κωδικό: "))

# Εύρεση μέσου όρου
vathSum = 0
for i in range(len(VATH)):
    vathSum += VATH[i]
mo = vathSum / len(VATH)
print (mo)

# Εύρεση μέγιστου βαθμού
maxVath = 0
for i in range(len(VATH)):
    if VATH[i] > maxVath:
        maxVath = VATH[i]
print (maxVath)

for i in range(len(VATH)):
    if VATH[i] == maxVath:
        print (KOD[i])

file = open("epityxon.txt", "w")
for i in range(len(VATH)):
    if VATH[i] > 60:
        file.write(str(i+1) + "." + KOD[i] + "\n")
file.close()