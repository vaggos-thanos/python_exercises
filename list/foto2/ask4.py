def bigword(list):
    max_len = len(list[0])
    max_str = ""
    for string in list:
        if len(string) > max_len:
            max_len = len(string)
            max_str = string

    return max_str

array = ["ra8y" , "tatatat" , "peroasdada" , "aaaa"]
print (bigword(array))