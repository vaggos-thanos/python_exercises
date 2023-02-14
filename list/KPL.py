#grade 1-100 int
#success >60
KOD = []
VATH = []
sun = 0
name = input("Enter your name: ").upper()
while name != "STOP":
    KOD.append(name)
    grade = int(input("Enter your grade: "))
    while grade < 0 or grade > 100:
        grade = int(input("Enter your grade: "))
    VATH.append(grade)
    name = input("Enter your name: ").upper()


for i in range(len(VATH)):
    sun += VATH[i]

mo = sun / len(VATH)
print ("The average is: ", mo)

meg = VATH[0]
for i in range(len(VATH)):
    if VATH[i] > meg:
        meg = VATH[i]
        max_name = KOD[i]
        
N = len(VATH)
i = 1
isSorted = False
while i < N and not isSorted:
    isSorted = True
    for i in range(N-1 , i-1 , -1):
        if VATH[i] > VATH[i-1]:
            VATH[i] , VATH[i-1] = VATH[i-1] , VATH[i]
            KOD[i] , KOD[i-1] = KOD[i-1] , KOD[i]
            isSorted = False
maxPeople = []
maxGrades = []
i = 0           
while VATH[i] == meg:
    maxPeople.append(KOD[i])
    maxGrades.append(VATH[i])
    i += 1
    
print ("The best student is/are: ", maxPeople, "with grade: ", maxGrades)

j = 1
arxeio = open(epityxon.txt, "w")
for i in range(len(VATH)):
    if VATH[i] >= 60:
        arxeio.write(str(j) + " " + KOD[i]) 
        j += 1
        
arxeio.close()

    
    
    
    
    
    