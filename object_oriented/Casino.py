class Casino:
    def __init__(self , cid , money_in , moneyout):
        self.cid = cid
        while money_in < 0:
            money_in = int(input("Money in must be positive number! Try again: "))
        self.money_in = money_in
        while moneyout < 0:
            moneyout = int(input("Money out must be positive number! Try again: "))
        self.moneyout = moneyout
        
    def win_lose(self):
        if self.money_in < self.moneyout:
            return "Win" + " " + str(self.moneyout - self.money_in)
        elif self.money_in > self.moneyout:
            return "Lose" + " " + str(self.money_in - self.moneyout)
        else:
            return "Draw" + " " + str(self.money_in)
        
        
    @staticmethod
    def quest():
        cid = str(input("CID= "))
        return cid in [i.cid for i in players]
        
players = []
for i in range(3):
    players.append(Casino(str(input("CID= ")) , int(input("Money in= ")) , int(input("Money out= "))))
    
for i in players:
    print (i.cid , i.win_lose())

    
print (Casino.quest())

    
    
        
    