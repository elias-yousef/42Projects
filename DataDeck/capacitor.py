import ex1

if __name__ == "__main__":
    print("Testing Creature with healing capability")

    print("base:")
    Sproutling = ex1.HealingCreatureFactory()
    first = Sproutling.create_base()
    print(first.describe())
    print(first.attack())
    print(first.heal("small"))

    print("evolved:")
    Bloomelle = ex1.HealingCreatureFactory()
    second = Bloomelle.create_evolved()
    print(second.describe())
    print(second.attack())
    print(second.heal("large"))

    print("\nTesting Creature with transform capability")
    print("base:")
    Shiftling = ex1.TransformCreatureFactory()
    third = Shiftling.create_base()
    print(third.describe())
    print(third.attack())
    print(third.transform())
    print(third.attack())
    print(third.revert())

    print("evolved:")
    Morphagon = ex1.TransformCreatureFactory()
    forth = Morphagon.create_evolved()
    print(forth.describe())
    print(forth.attack())
    print(forth.transform())
    print(forth.attack())
    print(forth.revert())
