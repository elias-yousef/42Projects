class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"Created:  {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    my_plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 333),
        Plant("Cactus", 60, 22),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in my_plants:
        plant.print_info()
    print(f"Total plants created: {len(my_plants)}")
