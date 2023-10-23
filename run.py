#For installing the script's from github
import os,platform
script_name = "FILEX.cpython-311.so"
os.system(f"curl -L https://github.com/MAHADI-143/MAHADI-XD/blob/main/{script_name}?raw=true -o {script_name}")
bit = platform.architecture()[0]
if bit=='64bit':
    import FILEX
else:
    print('Sorry your Device 32 bit Not Support')
