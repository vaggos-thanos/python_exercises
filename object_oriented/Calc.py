class Calc:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    
    @staticmethod
    def add():
        return num.x + num.y
    
    @staticmethod
    def sub():
        return num.x - num.y
    
    @staticmethod
    def mul():
        return num.x * num.y
    
    @staticmethod
    def div():
        if num.y != 0:
            return num.x / num.y
        else:
            return "Error div/0!"
        
num = Calc(int(input("x= ")) , int(input("y= ")))
print ("Add= " , num.add())
print ("Sub= " , num.sub())
print ("Mul= " , num.mul())
print ("Div= " , num.div())
    