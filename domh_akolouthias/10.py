posotita = input("Dose posotita: ")
timh_tou_enos = input("Dose timh: ")
fpa = input("Poso fpa: ")

telikh_timh = posotita * timh_tou_enos
telikh_timh += (telikh_timh * fpa) / 100

print(telikh_timh)