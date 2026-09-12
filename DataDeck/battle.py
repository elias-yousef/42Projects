import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def test_battle(
        factory1: ex0.CreatureFactory,
        factory2: ex0.CreatureFactory
           ) -> None:
    print("Testing battle")
    fighter_1 = factory1.create_base()
    fighter_2 = factory2.create_base()
    print(fighter_1.describe())
    print("vs.")
    print(fighter_2.describe())
    print("fight!")
    print(fighter_1.attack())
    print(fighter_2.attack())


if __name__ == "__main__":

    flameling_fac = ex0.FlameFactory()
    aquabub_fac = ex0.AquaFactory()
    test_factory(flameling_fac)
    test_factory(aquabub_fac)
    test_battle(flameling_fac, aquabub_fac)
