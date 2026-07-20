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
    for name, ready in DEPENDENCIES:
        try:
            importlib.import_module(name)
            version = metadata.version(name)
            print(f"[OK] {name} {version} - {ready}")
        except (ImportError, metadata.PackageNotFoundError):
            print(f"[MISSING] {name} - Not installed")
            all_valid = False
    return all_valid

def print_instructions() -> None:
    print("")
    print("To install it whith pip:")
    print("pip install -r requirements.txt")
    print("To install it whith Poetry:")
    print("  poetry install")


# Will simulate a program that analyzes meteorological data

def analyze_data() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    days = np.arange(365 * 25)
    dates = pd.date_range("2000-01-01",periods=len(days))
    
    base_temperature = 15
    season = np.sin((2 * np.pi * days / 365) - np.pi / 2)
    season_amplitude = 10
    noise = np.random.normal(0, 2, size=len(days))
    trend = np.linspace(0, 1.5, len(days))
    temperature = base_temperature + season_amplitude * season + noise + trend
    df = pd.DataFrame({
        "date": dates,
        "temperature": temperature
        })
    df["year"] = df["date"].dt.year
    yearly = df.groupby("year")["temperature"].mean()
    print("Analyzing meteorological data of the last 25 years...")
    print(f"Processing {len(df)} data points...")   
    print()
    print(f"Average temperature: {df['temperature'].mean():.2f} ºC")
    print(f"Maximum temperature: {df['temperature'].max():.2f} ºC")
    print(f"Minimum temperature: {df['temperature'].min():.2f} ºC")
    print(yearly)

    print("\nGenerating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(yearly.index, yearly.values)
    plt.title("Average yearly temperature")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")



if __name__ == "__main__":
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    if not valid_dependencies():
        print_instructions()
    else:
        analyze_data()