def trimSpaces(phrase):
    result = ""
    for char in phrase:
        if char != " ":
            result += char
    
    return result

def trimSpaces1(phrase):
    result = ""
    for i in range(len(phrase)):
        if phrase[i] != " ":
            result += phrase[i]
    return result

#main program
phrase = "Houston we have a problem"
print trimSpaces(phrase)
print trimSpaces1(phrase)