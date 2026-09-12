class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height_cm = height
        self.age_days = age

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height_cm += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height_cm}cm, {self.age_days} days old")


if __name__ == "__main__":
    plant_one = Plant("Rose", 25, 30)
    total_grow = 0
    print("=== Day 1 ===")
    plant_one.get_info()
    for _ in range(6):
        plant_one.age()
        plant_one.grow()
        total_grow += 1
    print("=== Day 7 ===")
    plant_one.get_info()
    print(f"Growth this week: +{total_grow}cm")
