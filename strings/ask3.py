def count_vowels(word):
    vowels = "AEIOUaeiou"
    count = 0
    for leter in word:
        if leter in vowels:
            count += 1
    return count

#main program
word = 'strawberries'
print count_vowels(word)