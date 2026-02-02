import sys
import os

# Add current folder to path so Python sees it
sys.path.append(os.getcwd())

print("--- DIAGNOSTIC START ---")

try:
    import extension
    print(f"1. File 'extension.py' found: {extension.__file__}")

    if hasattr(extension, 'VendorTableExtension'):
        print("2. Class 'VendorTableExtension' FOUND successfully.")
        cls = extension.VendorTableExtension
        if hasattr(cls, 'get_descriptor'):
            print("3. Descriptor FOUND. The code is perfect.")
        else:
            print("3. FAILURE: The class exists, but is missing the @web_app decorator.")
    else:
        print("2. FAILURE: File exists, but class 'VendorTableExtension' is MISSING inside it.")
        print("   Content of file seen by Python:", dir(extension))

except ImportError as e:
    print(f"1. FAILURE: Could not import 'extension.py'. Error: {e}")

print("--- DIAGNOSTIC END ---")
