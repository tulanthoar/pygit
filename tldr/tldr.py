from sys import argv
from urllib3.util.url import parse_url
from pyperclip import paste
from path import Path, getcwdu
from sh import wget
import tarfile

target = ''
tarname = 'temporary_tar'
if len(argv) == 2:
    target = argv[1]
elif len(argv) > 2:
    target = argv[1]
else:
    target = paste()
if target == '':
    print('no clipboard or args for target')
if not Path(target).exists():
    wget(target, O=tarname)
    maybeU = parse_url(target)
    maybeF = maybeU.path.split('/')[-1]
    targetF = getcwdu() + '/' + maybeF.split('.')[0]
else:
    Path(target).move(tarname)
    targetF = target.split('/')[-1]
    targetF = getcwdu() + '/' + targetF.split('.')[0]
with tarfile.open(tarname) as tf:
    tf.extractall()
Path(tarname).remove()
print(Path(targetF), end='')
