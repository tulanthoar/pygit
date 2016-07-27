#! /bin/env python3
with open( 'wallet.json', "r+" ) as f:
    data = f.read()
    f.seek( 0 )
    data = data.replace( '"' , '' )
    data = data.replace( '{' , '' )
    data = data.replace( '}' , '' )
    data = data.split( ',' )
    for p in data:
      p = p.split( ':' )
      f.write( p[1].strip() + '\n' )
    f.truncate()
