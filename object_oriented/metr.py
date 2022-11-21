class Metr:
    ano = 20
    kato = 1

    def __init__(self, i):
        if(i > Metr.ano):
            self.i = Metr.ano
        elif (i < Metr.kato):
            self.i = Metr.kato
        else:
            self.i = i

        print( "Metr created with value: " + str(self.i)) 

    def auxisi(self):
        print(self.i)
        if(self.i < Metr.ano):
            self.i += 1

    def miosi(self):
        if(self.i > Metr.kato):
            self.i -= 1

    def print_metr(self):
        print(self.i)

# Path: object_oriented/program.py
metr1 = Metr(12)
metr1.auxisi()
metr1.print_metr()
metr1.miosi()
metr1.print_metr()