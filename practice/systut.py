import sys
import time
def count( n ):
  t1 = time.time()
  for i in range( 0, n ):
    print( i )
    time.sleep( 0.1 )
  print( str( time.time() - t1 ) )
count( 5 )
print( time.time() )
print( time.asctime() )
print( time.localtime() )
at = time.asctime()
t = time.localtime()
yr=t[0]
dy=t[2]
mnth = at[4:7]
print( str( dy ) + '-' + str( mnth ) + '-' + str( yr ) )
inp = sys.stdin.readline()
print( inp )
inp5 = sys.stdin.readline( 5 )
print( inp5 )
sys.stdout.write( inp5 + 'sys' )
print( sys.version )
