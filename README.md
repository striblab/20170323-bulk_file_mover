# Bulk file mover

by [Frey Hargarten](https://github.com/jeffhargarten)

Moves all files according to specific titles to the desired folders. Requires [Python3](https://www.python.org/download/releases/3.0/).

### Usage:

1. Edit these lines in the script to fit your needs. 


```bash
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
$ python3 know_count.py <filename>
```

2. run script


```bash
$ python3 bulk_file_mover.py <filename>
```
