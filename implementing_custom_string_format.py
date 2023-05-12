# implementing Custom string 

class Person:
    def __init__(self,name):
        self.name = name 
    def __format__(self, format_spec):
        if format_spec == "scream":
            return self.name.upper() + "!"
        elif format_spec == "repeat":
            return self.name * 3
        return self.name
p = Person("sobhan")
print(f"{p}")
print(f"{p:scream}")
print(f"{p:repeat}")