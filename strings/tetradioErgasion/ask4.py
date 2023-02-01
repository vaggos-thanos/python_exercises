sentence = ""
word = raw_input("give word")
while word != ".":
    sentence += word + " "
    word = raw_input("give word")
else:
    sentence += "."

print(sentence)