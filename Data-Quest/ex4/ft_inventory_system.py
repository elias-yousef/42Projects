import sys


def main() -> None:
    print("== Inventory System Analysis ===")
    dict_items = {}
    if len(sys.argv) == 0:
        raise Exception("No argument provided")
    for arg in sys.argv:
        if arg != sys.argv[0]:
            item = arg.split(":")
            if item[0] in dict_items:
                print(f"Redundant item {item[0]} - discarding")
                continue
            try:
                dict_items[item[0]] = int(item[1])
            except ValueError:
                print(f"Quantity error for {item[0]}: invalid literal \
for int() with base 10: {item[1]}")
            except IndexError:
                print(f"Error - invalid parameter {item[0]}")
    sum_value = sum(dict_items.values())
    print(f"Got inventory: {dict_items}")
    print(f"Item list: {list(dict_items.keys())}")
    print(f"Total quantity of the {len(dict_items)} items: \
{sum_value}")
    for items in dict_items:
        print(f"Item {items} represents \
{round(dict_items[items] / sum_value * 100, 1)}%")
    max_value = max(dict_items.values())
    for items in dict_items:
        if dict_items[items] == max_value:
            max_item = items
            break
    min_value = min(dict_items.values())
    for items in dict_items:
        if dict_items[items] == min_value:
            min_item = items
            break
    print(f"Item most abundant: {max_item} with \
quantity {max_value}")
    print(f"Item least abundant: {min_item} with quantity {min_value}")
    dict_items.update({'magic_item': 1})
    print(f"Updated inventory: {dict_items}")


try:
    main()
except Exception as e:
    print(e)
