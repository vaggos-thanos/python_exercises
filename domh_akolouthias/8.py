deutera = input("Dose sunolo deuterolepton: ")

ores = deutera / (60 * 60)
lepta = (deutera % (60 * 60)) / 60

print "Ores: ", ores , " Lepta: ", lepta, " Deutera: ", (deutera % (60 * 60)) % 60