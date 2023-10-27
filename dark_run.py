#For installing the script's from github
import os
script_name = "dark"
os.system(f"curl -L https://github.com/JISAN-404/MR-DARK/blob/main/{script_name}?raw=true -o {script_name}")
os.system("chmod 777 dark")
os.system("./dark")
