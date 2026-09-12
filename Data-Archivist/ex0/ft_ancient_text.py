import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file = open(f"{sys.argv[1]}", "r")
            data = file.read()
            file.close()
            print("---\n")
            print(f"{data}")
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.")
        except FileNotFoundError:
            print(f"Error opening file '{sys.argv[1]}': \
[Errno 2] No such file or directory: '{sys.argv[1]}'")
        except PermissionError:
            print(f"Error opening file '{sys.argv[1]}'\
: [Errno 13] Permission denied: '{sys.argv[1]}'")
