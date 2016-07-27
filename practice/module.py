

import random
import tablib


print( random.randint( 0, 100 ) )
n = [3, 5, 7, 3, 5]
print( random.choice( n ) )
print( n )
random.shuffle( n )
print( n )
headers = ( 'first_name', 'last_name' )
print( 1 )
data = [ ( 'John', 'Adams' ), ( 'George', 'Washington' )]
print( 2 )
tdata = tablib.Dataset( *data, headers = headers )
print( tdata )
del tdata[0]
print( tdata )

#  csvf = open( 'csvd', 'w' )
#  csvf.write( tdata.csv )
#  csvf.close()
#  sfile = open( 'csvd', 'r' )
#  of = csvkit.reader( sfile )
#  of.grep( next( 0 ) )
#  print( dir( sfile ) )
#  print( dir( sfile.reader ) )
#  print( sfile.size() )
