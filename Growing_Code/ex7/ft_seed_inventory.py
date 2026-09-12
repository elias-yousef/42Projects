def ft_seed_inventory(plant: str, num: int, type: str) -> None:
    if type == "grams":
        print(f"{plant.capitalize()} seeds: {num} grams total")
    elif type == "packets":
        print(f"{plant.capitalize()} seeds: {num} packets available")
    elif type == "area":
        print(f"{plant.capitalize()} seeds: covers {num} square meters")
