import sys
import os


def detect_dependency_manager() -> str:
    if os.path.exists("poetry.lock"):
        return "Poetry (Managed Environment)"
    else:
        return "pip (Standard Environment)"


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    manager = detect_dependency_manager()
    print(f"Environment detected: {manager}")
    all_pack = True
    try:
        import numpy as np
        np_ver = np.__version__
        np_status = f"[OK] numpy ({np_ver}) - Numerical computation ready"
    except ImportError:
        all_pack = False
        np_status = "[MISSING] numpy - Required for generating Matrix data"
    try:
        import pandas as pd
        pd_ver = pd.__version__
        pd_status = f"[OK] pandas ({pd_ver}) - Data manipulation ready"
    except ImportError:
        all_pack = False
        pd_status = "[MISSING] pandas - Required \
for structured data dataframes"
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        plt_ver = matplotlib.__version__
        plt_status = f"[OK] matplotlib ({plt_ver})) - Visualization ready\n"
    except ImportError:
        all_pack = False
        plt_status = "[MISSING] matplotlib - Required for generating charts"

    print(np_status)
    print(pd_status)
    print(plt_status)

    if not all_pack:
        print("LOADING STATUS: Error - Missing core dependencies.")
        sys.exit(1)

    print("Analyzing Matrix data...\n")
    y_axis = np.random.normal(0, 1, 1000)
    x_axis = np.arange(0, 1000)

    print("Processing 1000 data points...")
    my_var = pd.DataFrame({'x': x_axis, 'y': y_axis})

    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(my_var['x'], my_var['y'], label='Random Data', color='blue')
    plt.title('Analysis of Random Data (0-1000)')
    plt.xlabel('X-axis')
    plt.ylabel('Random Values')
    plt.savefig('matrix_analysis.png')
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
