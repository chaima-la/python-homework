class Car :
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.year = year
        self.model=model
    def engine(self):
        print("engine starts")
    def details(self):
        return f"the car's model{self.model}and the year{self.year}and make{self.make}"

car = Car("make1","model1","year1")
car.engine()
print(car.details())
