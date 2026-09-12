def intt(string: str) -> None:
    for num in string:
        if num not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            raise ValueError


def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        intt("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file ’missing.txt’\n")
    try:
        print("Testing KeyError...")
        garden = {"tomato": 1}
        print(garden["lettuce"])
    except KeyError:
        print("Caught KeyError: ’missing_plant’\n")
    try:
        print("Testing multiple errors together...")
        10 / 0
    except Exception:
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
