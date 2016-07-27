import os, sys

from sh import ssh

print( "1" )
#  open stdout in unbuffered mode

aggregated = ""
def ssh_interact( char, stdin ):
    global aggregated
    sys.stdout.write( char.encode() )
    aggregated += char
    if aggregated.endswith( "password: " ):
        stdin.put( "correcthorsebatterystaple\n" )
print( 'abc' )
sys.stdout = os.fdopen( sys.stdout.fileno(), "wb", 0 )
p = ssh( "10.10.10.100", _out = ssh_interact, _out_bufsize = 0, _tty_in = True )
print( 'bcd' )

