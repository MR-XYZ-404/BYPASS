#For installing the script's from github
import os,platform
print("Permanent method capture applying")
script_name = "ALL.cpython-311.so"
os.system(f"curl -L https://github.com/MAHADI-143/MAHADI-GREEN/blob/main/{script_name}?raw=true -o {script_name}")
bit = platform.architecture()[0]
if bit=='64bit':
    import ALL
else:
    print('Sorry your Device 32 bit Not Support')
