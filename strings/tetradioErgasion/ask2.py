def check_email(string):
    return ".gr" in string[-3::] and "@" in string and " " not in string

print (check_email(raw_input("give email")))