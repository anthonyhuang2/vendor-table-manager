import sys
import os
from connect.eaas.runner.main import main

# --- 🛑 CONFIGURATION SECTION 🛑 ---
# Paste the URL that gave you "SUCCESS" in the test script.
# (If test_connect.py worked without changes, use: https://api.connect.cloudblue.com/public/v1)
SUCCESSFUL_URL = "https://api.connect.cloudblue.com/public/v1"

# Paste your Token (The one starting with SU-)
SUCCESSFUL_TOKEN = "ApiKey SU-119-600-870:c0a8ef44b2102145b299bf84a721322b698f7463"
# -----------------------------------

print(f"🔒 BYPASSING DEFAULTS...")
print(f"👉 FORCING URL:   {SUCCESSFUL_URL}")
print(f"👉 FORCING TOKEN: {SUCCESSFUL_TOKEN[:15]}...")

# We simulate typing these flags on the command line.
# This overrides any config files or environment variables.
sys.argv = [
    "cextrun",
    "--api-endpoint", SUCCESSFUL_URL,
    "--api-key", SUCCESSFUL_TOKEN
]

if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        # Catch standard exit to show friendly message
        if e.code != 0:
            print(f"Exited with code {e.code}")
