import os
myf = input( "enter name " )
print( myf )
f = open( myf )
newf = open( "copyf", 'w' )
newf.write( f.read() )
f.close()
newf.close()
