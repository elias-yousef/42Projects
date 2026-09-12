import sys

if __name__ == "__main__":
    list_of_numbers = []
    print("=== Player Score Analytics ===")
    for arg in sys.argv:
        if arg == sys.argv[0]:
            pass
        else:
            try:
                converted = int(arg)
                list_of_numbers.append(converted)
            except ValueError:
                print(f"Invalid parameter: {arg}")
    num_of_arg = len(list_of_numbers)
    Average_score = 1.0
    if num_of_arg != 0:
        print(f"Scores processed: {list_of_numbers}")
        Average_score = sum(list_of_numbers) / num_of_arg
        print(f"Total players: {num_of_arg}")
        print(f"Total score: {sum(list_of_numbers)}")
        print(f"Average score: {Average_score}")
        print(f"High score : {max(list_of_numbers)}")
        print(f"Low score : {min(list_of_numbers)}")
        range_num = max(list_of_numbers) - min(list_of_numbers)
        print(f"Score range: {range_num}")
    if num_of_arg == 0:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
