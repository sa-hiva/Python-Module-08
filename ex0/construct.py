import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("VirtualEnvironment: None detected")
        print()
        print("""WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv your_environment_name
source your_evironment_name/bin/activate # On Unix
your_environment_name\\Scripts\\activate # On Windows

Then run this program again.""")
    else:
        venv_name = os.path.basename(sys.prefix)
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"VirtualEnvironment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("""SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.""")
        print("")
        print("Package installation path:")
        print(site.getsitepackages()[0])
