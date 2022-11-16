class Roloi:
    def __init__(self, wr, lep, deft):
        while wr > 23 or wr < 0:            
            wr = int(input("Give correct hours: "))

        while lep > 59 or lep < 0:            
            lep = int(input("Give correct minutes: "))
        
        while deft > 59 or deft < 0:            
            deft = int(input("Give correct seconds: "))

        self.wr = wr
        self.lep = lep
        self.deft = deft
    
    def time(self):
        return(str(self.wr) + ":" + str(self.lep) + ":" + str(self.deft))
    
    def give_secs(self):
        return((self.wr * 60 * 60) + (self.lep * 60) + self.deft)

roloi = Roloi(28, 710, 40000)
print(roloi.time())
print(roloi.give_secs())