import subprocess
import sys

# List of required packages
packages = [
    'requests', 
    'beautifulsoup4', 
    'pandas', 
    'csv'  # csv is part of the Python standard library, no need to install it separately
]

# Check and install missing packages
for package in packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Create requirements file
with open('requirements.txt', 'w') as f:
    for package in packages:
        f.write(f"{package}\n")
        
        # Install packages from requirements file
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])