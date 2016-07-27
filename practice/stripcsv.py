import os
csvf = open( "txt", 'r' )
nocomm = open( 'nocomma', 'w' )
starttext = csvf.read()
print( starttext )
i = 0
stop = False
for i in range( 0, len( starttext ) ):
  if starttext[i] == ',':
    stop = True
  if starttext[i] == '\n':
    stop = False
#    nocomm.write( '\n' )
  if stop == False:
    nocomm.write( starttext[i] )
print( starttext )
csvf.close()
nocomm.close()
nocomm = open( 'nocomma', 'r' )
print( nocomm.read() )
nocomm.close()