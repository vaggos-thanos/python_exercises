class CheeseCompany:
    fpa = 24 * 0.01
    def __init__(self, cheese, fat, price):
        self.cheese = cheese
        self.fat = fat
        if price < 0:
            self.price = 10
        else:
            self.price = price
        
    def telikhTimi(self):
        return self.price + self.price * self.fpa
    
    def showCheese(self):
        print("Cheese Type: " + self.cheese + " Fat: " + str(self.fat) + " Price: " + str(self.price) + " Telikh Timi: " + str(self.telikhTimi()))
    
    @classmethod
    def setFpa(cls, fpa):
        cls.fpa = fpa * 0.01
    
    @staticmethod
    def searchCheese(cheese, cheeseList):
        for c in cheeseList:
            if c.cheese == cheese:
                return True
        return False
    
cheeseList = []

cheeseList.append(CheeseCompany("Feta", 20, 14))
cheeseList.append(CheeseCompany("Manouri", 35, 12))
cheeseList.append(CheeseCompany("Entam", 27, 13))
cheeseList.append(CheeseCompany("GKOUNTA", 26, 11))
cheeseList.append(CheeseCompany("Emental", 28, 15))

for c in cheeseList:
    c.showCheese()

CheeseCompany.setFpa(21)

print(CheeseCompany.searchCheese("Feta", cheeseList))