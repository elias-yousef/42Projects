class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def display_info(self) -> None:
        print(f"- {self.name} Tree : {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.color = flower_color

    def display_info(self):
        print(f"- {self.name}: {self.height}cm, \
{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize = prize_points

    def display_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} \
flowers (blooming), Prize points: {self.prize}")


class GardenManager:
    total_garden = 0

    def __init__(self, manager_name: str) -> None:
        self.manager = manager_name
        self.plants = []
        GardenManager.total_garden += 1

    @staticmethod
    def Height_test(height: int) -> str:
        if height > 0:
            return "Height validation test: True"
        else:
            return "Height validation test: False"

    class GardenStats:
        def calc_score(self, garden: "GardenManager") -> int:
            total = 0
            for plants in garden.plants:
                total += plants.height
                if type(plants) is PrizeFlower:
                    total += plants.prize
            return total

        def generate_report(self, garden: "GardenManager") -> None:
            type1 = 0
            type2 = 0
            type3 = 0
            number = len(garden.plants)
            print(f"\n=== {garden.manager} Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                plant.display_info()
            print(f"\nPlants added: {number} Total growth: {number}cm")
            for plant in garden.plants:
                if type(plant) is PrizeFlower:
                    type3 += 1
                elif type(plant) is FloweringPlant:
                    type2 += 1
                elif type(plant) is Plant:
                    type1 += 1
            print(f"Plant types: {type1} regular, \
{type2} flowering, {type3} prize flowers\n")

    def grow_all_plants(self) -> None:
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_garden}")

    def add_plant(self, plants: Plant) -> None:
        self.plants.append(plants)
        print(f"Added {plants.name} to {self.manager} garden")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    Alice = GardenManager("Alice")
    bob = GardenManager("bob")
    test1 = Plant("Oak", 100)
    test2 = FloweringPlant("Rose", 25, "red")
    test3 = PrizeFlower("Sunflower", 50, "yellow", 10)
    Alice.add_plant(test1)
    Alice.add_plant(test2)
    Alice.add_plant(test3)
    print("")
    Alice.grow_all_plants()
    info1 = GardenManager.GardenStats()
    info1.generate_report(Alice)
    print(GardenManager.Height_test(info1.calc_score(Alice)))

    print("=====================================")

    bob.add_plant(test1)
    bob.add_plant(test2)
    bob.add_plant(test3)
    print("")
    bob.grow_all_plants()
    info2 = GardenManager.GardenStats()
    info2.generate_report(bob)
    print(GardenManager.Height_test(info2.calc_score(bob)))
    print(f"Garden scores - Alice {info1.calc_score(Alice)}, \
bob {info2.calc_score(bob)}")
    print(f"Total gardens managed: {GardenManager.total_garden}")
