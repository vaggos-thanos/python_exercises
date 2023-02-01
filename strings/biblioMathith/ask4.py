def isSubstring(string , substring):
    return (substring == string)

def counter(string, subString):
    count = 0
    newString = ''

    for ii in range(len(string)):
        lengthSub = len(subString) - 1 + ii
        newString = ''
        for i in range(ii - 1, lengthSub):
            newString += string[i]
        
        if(isSubstring(newString, subString)):
            count += 1
    return count

print counter('vaggoggs', 'gg')