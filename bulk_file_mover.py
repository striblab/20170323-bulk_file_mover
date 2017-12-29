import shutil
import os

#path of the source folder
source = '/path/to/source_folder'

#path of destination folders, add more at your leisure
dest1 = '/path/to/example1_folder_name'
dest2 = '/path/to/example2_folder_name'

files = os.listdir(source)

#change the search criteria to your liking
for f in files:
    if (f.startswith("Example1") or f.startswith("example1")):
        shutil.move(f, dest1)
    elif (f.startswith("Example2") or f.startswith("example2")):
        shutil.move(f, dest2)