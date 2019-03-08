from os import listdir
from os import system
from os.path import isfile, join
import sys
import glob

dirFileList = glob.glob(f"{sys.argv[1]}\\**\\*.cfg", recursive=True)

for currFile in dirFileList:
    print(f"processing file {currFile}...")
    system(f"py wmlindent \"{currFile}\"")