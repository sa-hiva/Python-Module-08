import importlib
from importlib import metadata

DEPENDENCIES: list[tuple[str, str]] = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
    ("matplotlib", "Visualization ready")
]

def valid_dependencies() -> bool:
    print("Checking dependencies:")
    all_valid = True
    for dependency in DEPENDENCIES:
        name = dependency[0]
        ready = dependency[1]
        try:
            importlib.import_module(name)
            version = metadata.version(name)
            print(f"[OK] {name} {version} - {ready}")
        except ImportError:
            print(f"[MISSING] {name} - Not installed")
            all_valid = False
    return all_valid

def print_instructions() -> None:
    print("")
    print("To install it whit pip:")
    print("pip install -r requirements.txt")
    print("To install it whith Poetry:")
    print("  poetry install")


# Will simulate a program that analyzes metheorological data

def analyze_data() -> None:
    import pandas as pd
    import numpy as np
    dates = pd.date_range("2000-01-01", periods=365)
    days = np.arrange(365 * 25)
    
    base_temperature = 15
    season = np.sin((2 * np.pi * days / 365) - np.pi / 2)
    season_amplitude = 10
    noise = np.random.normal(0, 2, size=365)
    trend = np.linspace(0, 1.5, 365)
    temperature = base_temperature + season_amplitude * season + noise


if __name__ == "__main__":
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    if not valid_dependencies():
        print_instructions()