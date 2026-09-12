import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        current_python: str = sys.executable
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\activate     # On Windows")
        print("\nThen run this program again.")

    else:
        venv_name: str = os.path.basename(sys.prefix)
        python_exe: str = sys.executable
        env_path: str = sys.prefix
        package_path = site.getsitepackages()[0]
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_exe}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}\n")
        print("""SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.\n""")
        print(f"Package installation path:\n{package_path}")
