def ft_count_harvest_recursive() -> None:
    num = input("Days until harvest: ")
    days = int(num)
    integer = 1

    def handle_rec(integer):
        if integer <= int(days):
            print(f"Day {integer}")
            handle_rec(integer + 1)
        else:
            print("Harvest time!")

    handle_rec(integer)
