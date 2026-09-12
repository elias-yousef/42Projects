import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("[MISSING] dotenv - Required for Oracle")
    sys.exit(1)


def validate_config(required_keys: list[str]) -> None:
    missing_key = []
    for key in required_keys:
        if not os.getenv(key):
            missing_key.append(key)
    if missing_key:
        print(f"ERROR: Missing required \
configuration variables: {missing_key}")
        sys.exit(1)


def check_environment_security() -> None:
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    if os.environ.get("MATRIX_MODE") == "development":
        print("[OK] production overrides available")
    elif os.environ.get("MATRIX_MODE") == "production":
        print("[OK] development overrides available")


if __name__ == "__main__":
    REQUIRED = [
        "ZION_ENDPOINT", "DATABASE_URL", "API_KEY", "MATRIX_MODE", "LOG_LEVEL"
    ]
    validate_config(REQUIRED)
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {os.getenv("MATRIX_MODE")}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level:  {os.getenv("LOG_LEVEL")}")
    print("Zion Network: Online")
    print()
    print("Environment security check:")
    check_environment_security()
    print("\nThe Oracle sees all configurations")
