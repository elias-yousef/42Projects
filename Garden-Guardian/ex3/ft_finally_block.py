def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plants in plant_list:
            if type(plants) is str:
                print(f"Watering {plants}")
            else:
                raise ValueError(f"Cannot water {plants} - invalid plant!")
    except ValueError as error:
        print(f"Error: {error}")
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    list1 = ["tomato", "lettuce", "carrots"]
    list2 = ["tomato", None]
    water_plants(list1)
    print("Testing with error...")
    water_plants(list2)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
