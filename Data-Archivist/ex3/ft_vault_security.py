def secure_archive(file_name: str, action: str = "r", data: str = "") -> tuple:
    try:
        if action == "r":
            with open(file_name, "r") as file:
                newdata = file.read()
            return (True, newdata)
        elif action == "w":
            with open(file_name, "w") as file:
                file.write("\n")
            return (True, "Content successfully written to file")
    except FileNotFoundError:
        return (False, f"[Errno 2] No such file or directory:'{file_name}'")
    except PermissionError:
        return (False, f"[Errno 13] Permission denied: ’{file_name}’")
    return (False, "")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("notexisting", "r"), "\n")
    print("Using ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("inaccessible"), "\n")
    print("Using ’secure_archive’ to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"), "\n")
    print("Using ’secure_archive’ to write previous content to a new file:")
    print(secure_archive("regular_file", "w"))
