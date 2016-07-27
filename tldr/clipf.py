from path import Path, getcwdu
from pyperclip import copy
from sys import argv

toCp = ''
if len(argv) == 1:
    toCp = getcwdu()
    copy(toCp)
else:
    for f in argv[1:]:
        if Path(f).isfile():
            with open(Path(f), 'r') as txt:
                toCp += txt.read()
    copy(toCp)
print(toCp)
