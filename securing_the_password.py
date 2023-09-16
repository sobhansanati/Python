symbol = {
        'a' : '!!',
        'b' : '@',
        'c' : '#',
        'd' : '$',
        'e' : '^',
        'f' : '}',
        'g' : ']',
        'h' : ')',
        'i' : '*',
        'j' : '=',
        'k' : '+',
        'l' : '-',
        'm' : '_',
        'n' : '>',
        'o' : '<',
        'p' : '.',
        'q' : '%',
        'r' : '&',
        's' : '(',
        't' : '{',
        'u' : '[',
        'x' : '?',
        'y' : ',',
        'z' : '|',
    
}

inp = input('enter a password with you name : ')
print('password you enter:',inp )
password = ""

for i in inp:
    for key , val in symbol.items():
        if i in key:
            password = password + val
print("Your password is :",password) 