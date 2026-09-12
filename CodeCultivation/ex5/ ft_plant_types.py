class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, \
{self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self, name: str, height: int, age:
            int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, \
{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: int, age: int,
            harvest_season: str, nutritional_value: str) -> None:
        self.harvest_season = harvest_season
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, \
{self.age} days, {self.harvest_season} harvest")
        print(f"{name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    my_flower = Flower("Rose", 25, 30, "red")
    my_flower.bloom()
    my_tree = Tree("Oak", 500, 1825, 50)
    my_tree.produce_shade()
    my_vegetable = Vegetable("tomato", 80, 90, "summer", "vitamin C")
