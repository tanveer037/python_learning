class Father:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address

    def get_address(self):
        return self.address
    

class Child(Father):
    def __init__(self,name, address, school) -> None:
        super().__init__(name, address)
        self.school = school 

    def get_school(self):
        return self.school

f1 = Father('Bob','Washington')
c1 = Child('Alice','New York','Central')
print(f1.get_address())
print(c1.get_address())
print(c1.get_school())