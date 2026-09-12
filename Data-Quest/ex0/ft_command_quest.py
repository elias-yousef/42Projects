import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    number_of_arg = len(sys.argv)
    loop = number_of_arg
    count = 1
    print("Program name: " + sys.argv[0])
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Arguments received: {number_of_arg - 1}")
    while loop > 1:
        print(f"Argument {count}: {sys.argv[count]}")
        count += 1
        loop -= 1
    print(f"total arguments: {number_of_arg}")
