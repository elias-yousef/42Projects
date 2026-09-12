import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file = open(f"{sys.argv[1]}", "r")
            data = file.read()
            file.close()
            print("---\n")
            print(f"{data}")
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.\n")
            print("Transform data:")
            print("---\n")
            upgraded_lines = []
            newdata = data.split("\n")
            for line in newdata:
                stamped_line = line + "#"
                upgraded_lines.append(stamped_line)
            fullline = "\n".join(upgraded_lines)
            print(f"{fullline}")
            print("\n---")
            fileName = input("Enter new file name (or empty): ")
            if len(fileName) == 0:
                print("Not saving data.")
            else:
                newfile = open(f"{fileName}", "w")
                newfile.write(fullline)
                print(f"Saving data to {fileName}")
        except FileNotFoundError:
            print(f"[STDERR] Error opening file '{sys.argv[1]}': \
[Errno 2] No such file or directory: '{sys.argv[1]}'")
        except PermissionError:
            print(f"[STDERR] Error opening file '{fileName}'\
: [Errno 13] Permission denied: '{fileName}'")
