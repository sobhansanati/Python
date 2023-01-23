
def convert (a):
    if a =='goodbye':
        print("goodbye"+"\U0001F61E")
    elif a=='hello':
        print("hello"+"\U0001F603")
    elif a=='hello' and 'goodbye':
        print("\U0001F603"+"\U0001F61E")
    else:
        print("invalid")
    main()
def main():
    b=input("Enter:")
    if b==":)":
        print("hello"+"\U0001F606")
    elif b==":(":
        print("goodbye"+"\U0001F61E")
    elif b==':)'and':(':
        print("hello"+"\U0001F606","goodbye"+"\U0001F61E")
    else:
        print("invalid")

a=input("Enter the your action:")
convert(a)
    
