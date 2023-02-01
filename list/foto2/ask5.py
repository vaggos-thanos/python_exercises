def vowels(string):
    count = 0
    vows = "AEIOUaeiou"
    for item in string:
        if item in vows:
            count += 1

    return count


def defi(array):
    max_word = ''
    for word in array:
        if len(max_word) < vowels(word):
            max_word = word
    return max_word + " has ", vowels(max_word), " vowels"

array = ["aegaeg", "aegag", "aekgha", "aeuhae"]
print(defi(array))