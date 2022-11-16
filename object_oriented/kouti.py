class Kouti:
    def __init__(self, platos, mhkos, ypsos):
        self.platos = platos;self.mhkos = mhkos;self.ypsos = ypsos
    def emfanisi_ogkou(self):
        return self.platos * self.mhkos * self.ypsos
    def emfanisi_diastaseon(self):
        return self.platos + self.mhkos + self.ypsos
Koutia = []
for i in range(0, 10):
    Koutia.append(Kouti(int(input("Give width: ")), int(input("Give length: ")), int(input("Give height: "))))
for i in range(0, len(Koutia)):
    kouti = Koutia[i]
    print("To kouti", i + 1 ,"exei diastash:", kouti.emfanisi_diastaseon())
    print("To kouti", i + 1 ,"exei ogo:", kouti.emfanisi_ogkou())