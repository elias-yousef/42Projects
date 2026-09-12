class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!\n")
    except GardenError as planterror1:
        print(f"Caught a GardenError: {planterror1}")
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!\n")
    except GardenError as planterror2:
        print(f"Caught a GardenError: {planterror2}")
    try:
        print("Testing catching all garden errors...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught a PlantError: {error}")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as watererror:
        print(f"Caught a WaterError: {watererror}")
    finally:
        print("All custom error types work correctly!")
