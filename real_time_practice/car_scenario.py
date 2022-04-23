class Car:
    def __init__(self, brand, color, price, mileage, seating_capacity):
        self.brand = brand
        self.color = color
        self.price = price
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def features(self):
        print(f"""Color of car : {self.color}\n Brand : {self.brand}
    Price : {self.price}\n mileage : {self.mileage} \n seating_capacity : {self.seating_capacity}""")


class MarutiSuzuki(Car):
    def __init__(self):
        super().__init__("Ertiga smart hybrid LXI", "Pearl Metallic Auburn Red", 812500, "45litres", 7)

    # Private Methods to encapsulate data and methods
    def __internalfeatures(self):
        self.length = "14.42 feet"
        self.width = "5.69 feet"
        self.height = "5.54 feet"
        self.wheel_base = "8.99 feet"
        self.cargo_volume = "209 Litres"
        self.engine = "1.5 Liter cylinder"
        self.No_of_engines = 4
        print(f"length of Ertiga {self.length}")
        print(f"No of engines in Ertiga : {self.No_of_engines}")

    def method(self):
        super().features()

    def internal_data(self):
        self.__internalfeatures()


obj = MarutiSuzuki()
obj.method()
# obj._MarutiSuzuki__internalfeatures()  # By Name Mangling, we can access private methods outside the class
obj.internal_data()  # Using Public method to access private method
