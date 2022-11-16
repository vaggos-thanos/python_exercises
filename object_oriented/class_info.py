class Info:
    def __init__(self, content):
        self.content = content

    def keimeno(self):
        self.content = str(input("Give a Text: "))

    def spaces(self):
        counter = 0
        for leter in self.content:
            if leter == " ":
                counter += 1
        return counter

    def lexeis(self):
        test = (self.content).split(" ")
        test1 = []
        for i in range(len(test)):
            if len(test[i]) != 0:
                test1.append(test[i])
        return len(test1)

    def fonienta(self):
        vauels = ["a", "e", "y", "u", "i", "o"]
        counter = 0
        for letter in self.content.lower():
            if letter in vauels:
                counter += 1
        return counter
        

    def gramata(self):
        return (len(self.content) - self.spaces())

    def find(self, char):
        if self.content.find(char) == 1:
            return True
        return False

    def replace(self, char, replacement):
        if self.find(char) == True:
            return self.content.replace(char, replacement)

        return False

text1 = Info("awer")

print(text1.lexeis())
print(text1.find("}"))
print(text1.gramata())
print(text1.replace("a", "}"))
print(text1.fonienta())