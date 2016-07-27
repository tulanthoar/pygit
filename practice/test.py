#  this is just a comment
from builtins import help
def inc( n ):
  return n + 1
def upperName( name ):
  print( "hi %s" % name.upper() )
print( 5 + 4 )
words = ['a', 'b', 'c']
print( words[1] )
dict = {"k1":1, "k2":2, "k3":3}
print( dict["k2"] )
print( dict["k3"] )
dict.clear()
print( dict )
dict = {"k1":1, "k2":2, "k3":3}
print( dict.keys() )
print( dict.values() )
dict = {"k1a":1}
dict2 = {"k1":1, "k2":2, "k3":3, "k4":4}
dict.update( dict2 )
print( dict )
tup = ( range( 0, 3 ) )
print( 'tup val' )
for t in tup:
  print( t )
if 5 > 2:
  print( 'l am great' )
else:
  print( 'the world is over' )
fbool = 0 > 1
print( fbool )
tbool = 5 == 5
print( tbool )
print( 'tuple' )
for t in tup:
  print( 'tup %d %s' % ( t, words[t] ) )
i = 0
while words[i] != 'c':
  print( 'i %d %s' % ( i, words[i] ) )
  i = inc( i )
for l in "python":
  if l == "o":
    continue
  print( l )
try:
  print( 'a' + 1 )
except:
  print( 'problem' )
upperName( "nate" )
print( "%d" % abs( -4 ) )
print( dir( [] ) )
array = []
print( help( array.count ) )
print( eval( "4+5+5" ) )
print( float( "8" ) )
print( list( range( 0, 3 ) ) )
print( sum( tup ) )
afile = open( "/root/pytest", 'r' )
ftext = afile.read()
print( ftext )
afile.seek( 0, 0 )
ftext = afile.read()
print( ftext )
afile.close()
wfile = open( "/root/pytestw", 'w' )
wfile.write( 'sfuff\n' )
wfile.close()
wfile = open( "/root/pytestw", 'a' )
wfile.write( 'more sfuff\n' )
wfile.close()
wfile = open( "/root/pytestw" )
import os
os.renames( "/root/pytestw", "/root/pytestwre" )
os.renames( "/root/pytestwre", "/root/pytestw" )
per1, per2, per3 = 'me', 'you', 'him'
