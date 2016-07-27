import bs4
import requests

morninf = ( 'http://flightaware.com/live/flight/SOO597', '597' )
nightBoi = ( 'http://flightaware.com/live/flight/AMF1062', '1062' )
nightMhr = ( 'http://flightaware.com/live/flight/SOO197', '197' )
flights = [morninf, nightBoi, nightMhr]
with requests.Session() as ses:
  for f in flights:
    p = ses.get( f[0] )
    soup = bs4.BeautifulSoup( p.text, 'html.parser' )
    parts = soup.title.string.split( '#' )
    fnum = parts[0] + f[1]
    btag = soup.body
    for t in btag.find_all( class_ = "track-panel-actualtime" ):
      ftimes = t.text
    for child in btag.find_all( class_ = "track-panel-arrival" ):
      for s in child.find_all( 'a' ):
        farr = s.text
    for child in btag.find_all( class_ = "track-panel-departure" ):
      for s in child.find_all( 'a' ):
        fdep = s.text
    print( ftimes )
    print( farr )
    print( fdep )
    for s in btag.find_all( class_ = "track-panel-inner" ):
#        for s2 in s.find_all( class_ = "secondaryHeader" ):
      for s2 in s.children:
#          print( str( s2 ) + '\n' )
        stt = [text for text in repr( s2 ).split( '<th' )]
#          print( stt )
        for stt2 in stt:
          if stt2.count( "Status" ) != 0:
#              print( stt2 )
            if ( stt2.count( "En Route" ) ) != 0:
              print( "In the air" )
            else:
              print( "not" )
