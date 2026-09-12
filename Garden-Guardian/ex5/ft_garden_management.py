class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class SunLightError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plants(self, plant: str) -> None:
        if not plant:
            raise PlantError("Plant name cannot be empty!\n")
        else:
            self.plants.append(plant)
            print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(
            self, water: int, sun:
            int, plant_name: str) -> None:
        if plant_name in self.plants:
            if water > 10:
                raise WaterError(f"Water level {water} is too high (max 10)\n")
            elif water < 1:
                raise WaterError(f"Water level {water} is too low (min 1)\n")
            if sun < 2:
                raise SunLightError(f"Sunlight hours \
{sun} is too low (min 2)\n")
            elif sun > 12:
                raise SunLightError(f" Sunlight hours \
{sun} is too high (max 12)\n")
            else:
                print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        else:
            raise PlantError(f"cannot find {plant_name} in the garden")

    def tank_level(self, water_level: int) -> None:
        if water_level < 30:
            raise GardenError("Not enough water in tank")
        else:
            print("water level is good")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden_one = GardenManager()
    try:
        garden_one.add_plants("tomato")
        garden_one.add_plants("apple")
        garden_one.add_plants("")
    except PlantError as error:
        print(f"Error adding plant: {error}")

    garden_one.water_plants()
    print("Checking plant health...")
    try:
        garden_one.check_plant_health(5, 5, "tomato")
    except GardenError as error:
        print(f"Error checking tomato: {error}")
    try:
        garden_one.check_plant_health(20, 6, "apple")
    except GardenError as error:
        print(f"Error checking banana: {error}")
    print("Testing error recovery...")
    try:
        garden_one.tank_level(20)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
