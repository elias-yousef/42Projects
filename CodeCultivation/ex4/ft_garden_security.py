class SecurePlant:
    def __init__(self, name: str):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name} ")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative day rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def print_info(self):
        print(f"Current plant: {self.name} \
({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_age(20)
    plant.set_height(30)
    plant.set_height(-20)
    plant.set_age(-5)
    plant.print_info()
