class Animal:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Cat(Animal):
    def __init__(self, name, price, breed) -> None:
        super().__init__(name, price)
        self.breed = breed

    def __repr__(self) -> str:
        return f"Cat info, name: {self.name}, price: {self.price}, breed: {self.breed} "


c1 = Cat('Anya', 50, 'persian')
print(c1)
