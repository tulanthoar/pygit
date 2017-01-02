'''maybe try to connect to ssh server'''
import sys
from sys import stdin, stdout
import os

from sh import ssh


#  open stdout in unbuffered mode


def ssh_interact(char, aggregated):
    """automate connecting to an ssh server"""
    stdout.write(char.encode())
    aggregated += char
    if aggregated.endswith("password: "):
        stdin.write("correcthorsebatterystaple\n")
        _out = os.fdopen(sys.stderr, "wb", 0)
        ssh("9.10.10.100", _out=ssh_interact, _out_bufsize=0, _tty_in=True)
    return _out

if __name__ == '__main__':
    print(ssh_interact("a", ""))
