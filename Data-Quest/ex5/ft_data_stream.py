import random
from typing import Generator

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swi\
m", "use", "release"]


def gen_event() -> Generator[tuple, None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        tuple_ply = (name, action)
        yield (tuple_ply)


def consume_event(player_list: list) -> Generator[tuple, None, None]:
    while len(player_list) > 0:
        remove = random.choice(player_list)
        player_list.remove(remove)
        yield remove


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generate = gen_event()
    player_list = []
    counter = 0
    counter_two = 10
    while counter < 1000:
        info = next(generate)
        print(f"Event {counter}: Player \
{info[0]} did action {info[1]}")
        counter += 1
    while counter_two > 0:
        info = next(generate)
        counter_two -= 1
        player_list.append(info)
    print(f"Built list of 10 events: {player_list}")
    for event in consume_event(player_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {player_list}")
