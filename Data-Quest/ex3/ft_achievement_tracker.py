import random


achiv_list = ["First Blood", "Novice Crafter", "Master Blacksmit\
h", "Dragon Slayer", "Pacifist", "Speed Demo\
n", "Completionist", "Loot Goblin", "Dungeon Maste\
r", "No Hit Run", "Lorekeeper", "Treasure Hunte\
r", "Survivor", "Sharpshooter", "Brawle\
r", "Master Alchemist", "Beastmaster", "Shadow Strike"]


def gen_player_achievements() -> set:
    num_of_achiv = random.randint(3, 9)
    each_player_achiv = random.sample(achiv_list, num_of_achiv)
    set_achiv = set(each_player_achiv)
    return (set_achiv)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    set_list = set(achiv_list)
    Alice = gen_player_achievements()
    print(f"Player Alice: {Alice}")
    Bob = gen_player_achievements()
    print(f"Player Bob: {Bob}")
    Charlie = gen_player_achievements()
    print(f"Player Charlie: {Charlie}")
    Dylan = gen_player_achievements()
    print(f"Player Dylan: {Dylan}\n")
    all_union = Alice.union(Bob).union(Charlie).union(Dylan)
    print(f"All distinct achievements: {all_union}\n")
    all_inters = Alice.intersection(Bob)
    new = all_inters.intersection(Charlie).intersection(Dylan)
    print(f"Common achievements: {new}\n")

    print(f"Only Alice has: \
{Alice.difference(Bob).difference(Dylan).difference(Charlie)}")
    print(f"Only bob has: \
{Bob.difference(Alice).difference(Dylan).difference(Charlie)}")
    print(f"Only Charlie has: \
{Charlie.difference(Bob).difference(Dylan).difference(Alice)}")
    print(f"Only Dylan has: \
{Dylan.difference(Bob).difference(Alice).difference(Charlie)}\n")

    print(f"Alice is missing: {set_list.difference(Alice)}")
    print(f"Bob is missing: {set_list.difference(Bob)}")
    print(f"Charlie is missing: {set_list.difference(Charlie)}")
    print(F"Dylan is missing: {set_list.difference(Dylan)}")
