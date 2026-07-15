import importlib, importlib_metadata

DEPENDENCIES = [
    ("pandas", "Data manipulation ready")
    ("numpy", "Numerical computation ready")
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
            version = importlib.metadata.version(name)
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


if __name__ == "__main__":
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    if not valid_dependencies():
        print_instructions()