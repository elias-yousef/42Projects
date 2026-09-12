def check_temperature(temp_str: str) -> int:
    try:
        temp_num = int(temp_str)
        if temp_num < 0:
            print(f"Error: {temp_num}°C is too cold for plants (min 0°C)\n")
        elif temp_num > 40:
            print(f"Error: {temp_num}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp_num}°C is perfect for plants!\n")
            return temp_num
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature_input()
