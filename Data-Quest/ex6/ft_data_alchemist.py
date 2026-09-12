import random

if __name__ == "__main__":
    first_list = ["Alice", "bob", "Charlie", "dylanc", "E\
mma", "Gregory", "john", "kevin", "Liam"]
    capitalized_list = [name.capitalize() for name in first_list]
    capitalized_only = [name for name in first_list if name.istitle()]
    score_list = {name: random.randint(1, 1000) for name in capitalized_list}
    average = round(sum(score_list.values()) / len(capitalized_list), 1)
    print(f"Initial list of players: {first_list}")
    print(f"New list with all names capitalized: {capitalized_list}")
    print(f"New list of capitalized names only: {capitalized_only}\n")
    print(f"Score dict: {score_list}")
    print(f"Score average is {average}")
    high_dict = {
        player: score
        for player, score in score_list.items()
        if score > average
        }
    print(f"High scores: {high_dict}")
