import ex0
import ex1
import ex2


def battle(
        opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]
        ) -> None:
    print("** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            if opponents[i] is opponents[j]:
                continue
            fac_a, strat_a = opponents[i]
            fac_b, strat_b = opponents[j]

            fighter_a = fac_a.create_base()
            fighter_b = fac_b.create_base()

            print(f"{fighter_a.describe()}\nvs.\n{fighter_b.describe()}")
            print("now fight!")
            try:
                strat_a.act(fighter_a)
                strat_b.act(fighter_b)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")

    fac1 = ex0.FlameFactory()
    fac2 = ex0.AquaFactory()
    fac3 = ex1.TransformCreatureFactory()
    fac4 = ex1.HealingCreatureFactory()

    stra1 = ex2.NormalStrategy()
    stra2 = ex2.AggressiveStrategy()
    stra3 = ex2.DefensiveStrategy()

    first_list = [(fac1, stra1), (fac4, stra3)]
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(first_list)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    second_list = [(fac1, stra2), (fac4, stra3)]
    battle(second_list)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    third_list = [(fac2, stra1), (fac4, stra3), (fac3, stra2)]
    battle(third_list)
