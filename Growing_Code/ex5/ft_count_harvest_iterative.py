def ft_count_harvest_iterative() -> None:
    days = 1
    num = input("Days until harvest: ")
    while days <= int(num):
        print(f"Day {days}")
        days += 1
    print("Harvest time!")
