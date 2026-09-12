import math


def get_player_pos() -> tuple:
    while True:
        counter = 0
        flage = True
        coordinate = input("Enter new coordinates as \
floats in format ’x,y,z’:")
        numlist = coordinate.split(",")
        new_list = []
        if len(numlist) != 3:
            print("Invalid syntax")
            continue
        for num in numlist:
            try:
                new_list.append(float(num))
            except ValueError:
                print(f"Error on parameter {numlist[counter]}: \
could not convert string to float: {numlist[counter]}")
                flage = False
            counter += 1
        if flage is False:
            continue
        else:
            mytuple = tuple(new_list)
            return (mytuple)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    mytuple = get_player_pos()
    print(f"Got a first tuple: {mytuple}")
    x1 = mytuple[0]
    y1 = mytuple[1]
    z1 = mytuple[2]
    distance = math.sqrt((x1-0)**2 + (y1-0)**2 + (z1-0)**2)
    print(f"It includes: x = {x1}, y = {y1}, z = {z1}")
    print(f"Distance to center: {round(distance, 4)}\n")
    print("Get a second set of coordinates")
    mytuple2 = get_player_pos()
    x2 = mytuple2[0]
    y2 = mytuple2[1]
    z2 = mytuple2[2]
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
