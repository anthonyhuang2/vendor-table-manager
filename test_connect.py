from connect.client import ConnectClient
from connect.client.exceptions import ClientError

# --- CONFIGURATION ---
# Replace this with your token
MY_TOKEN = "ApiKey SU-119-600-870:c0a8ef44b2102145b299bf84a721322b698f7463"

# Try the Global Endpoint first
MY_ENDPOINT = "https://api.connect.cloudblue.com/public/v1"
# ---------------------

print(f"📡 TESTING CONNECTION TO: {MY_ENDPOINT}")
print(f"🔑 USING TOKEN: {MY_TOKEN[:10]}...") 

client = ConnectClient(MY_TOKEN, endpoint=MY_ENDPOINT)

try:
    print("\nAttempting to verify token...")
    # We try to fetch the 'accounts' list, which is a standard safe check
    account = client.accounts.all().first()
    
    if account:
        print("\n✅ SUCCESS! Connection established.")
        print(f"   You are logged in as: {account['name']} (ID: {account['id']})")
        print("   This confirms the Token and URL are CORRECT.")
    else:
        print("\n⚠️  Connected, but no account info returned (Unusual, but not an error).")

except ClientError as e:
    print("\n❌ CONNECTION FAILED (ClientError)")
    print(f"   Error Code: {e.status_code}")
    print(f"   Message: {e}")
    
    if e.status_code == 401:
        print("\n🔎 DIAGNOSIS: 401 Unauthorized")
        print("   1. Your Token is invalid/expired.")
        print("   2. OR you are hitting the wrong region (US vs Europe).")
        print("   Try changing the endpoint in this script to:")
        print("   - https://api.connect.us.cloudblue.com/public/v1")
        print("   - https://api.connect.eu.cloudblue.com/public/v1")

except Exception as e:
    print(f"\n❌ CRITICAL FAILURE: {e}")
