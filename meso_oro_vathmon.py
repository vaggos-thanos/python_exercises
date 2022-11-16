def input_elexos():
    num = int(input("dose vathmo: "))
    while num <= 0:
        num = int(input("dose eguro vathmo: "))
    return num

sum = 0
for i in range(10):
    vathmos = input_elexos()
    sum += vathmos

mo = sum / 10.0
print (mo)
    