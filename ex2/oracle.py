import sys
import os


def load_config() -> tuple[dict[str, str], bool]:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        dotenv_loaded = True
    except ModuleNotFoundError:
        dotenv_loaded = False

    config = {
            "mode": os.environ.get("MATRIX_MODE", "unknown"),
            "database": os.environ.get("DATABASE_URL", "not configured"),
            "api_key": os.environ.get("API_KEY", "not configured"),
            "log_level": os.environ.get("LOG_LEVEL", "INFO"),
            "zion": os.environ.get("ZION_ENDPOINT", "not configured")
        }
    return config, dotenv_loaded


def mask(value: str) -> str:
    if len(value) <= 2:
        return "*" * len(value)
    return value[0] + "*" * (len(value) - 2) + value[-1]


def print_configuration(config: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    if config["mode"] == "development":
        print("Development environment detected.")
        print("Connected to local development database.")
        print("Debug features available.")
        print()
        print(f"Mode: {config['mode']}")
        print(f"Database: {config['database']}")
        print(f"API Access: {config['api_key']}")
        print(f"Log Level: {config['log_level']}")
        print(f"Zion Network: {config['zion']}")
    elif config["mode"] == "production":
        print("Production environment detected.")
        print("Production database selected.")
        print("Debug output disabled.")
        print("Optimized configuration loaded.")
        print()
        print(f"Mode: {config['mode']}")
        print(f"Database: {mask(config['database'])}")
        print(f"API Access: {mask(config['api_key'])}")
        print(f"Log Level: {config['log_level']}")
        print(f"Zion Network: {mask(config['zion'])}")
    else:
        print("Unknown environment detected.")
    print()


def security_check(config: dict[str, str]) -> None:
    print("Environment security check:")
    if os.path.exists(".env"):
        print("[OK] Environment configuration file detected")
    else:
        print("[WARNING] .env file not found")
    if config["mode"] == "development":
        print("[INFO] Running in development mode")
        print("[INFO] Verbose configuration output enabled")
    elif config["mode"] == "production":
        print("[OK] Production mode active")
        print("[OK] Sensitive configuration hidden")
    else:
        print("[WARNING] Unknown execution mode")


def print_instructions() -> None:
    print()
    print("[MISSING] python-dotenv package not installed")
    print()
    print("To install it use:")
    print("  pip install python-dotenv")
    print("  or")
    print("  pip install -r requirements.txt")
    print()


if __name__ == "__main__":
    config, dotenv_loaded = load_config()
    if not dotenv_loaded:
        print_instructions()
        sys.exit(1)
    print_configuration(config)
    security_check(config)
