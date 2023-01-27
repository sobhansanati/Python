def repeatesubstring(s):
    string = (s + s)[1:-1]
    print(string)
    return string.find(s) != -1 
print(repeatesubstring('abcabcabc'))
