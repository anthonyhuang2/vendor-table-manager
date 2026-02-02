import os
import sys

# --- FORCE CONFIGURATION (ALL VARIATIONS) ---
# We set every known variable name to ensure one of them hits.
TARGET_URL = "https://api.connect.cloudblue.com/public/v1"
TARGET_KEY = "SU-119-600-870:c0a8ef44b2102145b299bf84a721322b698f7463"

os.environ['API_ENDPOINT'] = TARGET_URL
os.environ['CONNECT_API_ENDPOINT'] = TARGET_URL  # <--- New standard
os.environ['SERVER_ADDRESS'] = TARGET_URL

os.environ['API_KEY'] = TARGET_KEY
os.environ['CONNECT_API_KEY'] = TARGET_KEY       # <--- New standard
# ---------------------------

print(f"🚀 FORCING ENDPOINT: {os.environ['CONNECT_API_ENDPOINT']}")

# Import and run
from connect.eaas.runner.main import main

if __name__ == '__main__':
    # Force the library to see the changes by reloading if needed
    try:
        sys.exit(main())
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
