class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant_one = Plant("Rose", 25, 30)
    plant_two = Plant("Sunflower", 80, 45)
    plant_three = Plant("Cactus", 15, 120)
    plant_one.print_info()
    plant_two.print_info()
    plant_three.print_info()
