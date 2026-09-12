def ft_harvest_total() -> None:
    days = 0
    total = 0
    while days < 3:
        num = input(f"Day {days} harvest: ")
        total += int(num)
        days += 1
    print(f"Total harvest: {total}")
