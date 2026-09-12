def ft_plant_age() -> None:
    num = input("Enter plant age in days: ")
    if int(num) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
