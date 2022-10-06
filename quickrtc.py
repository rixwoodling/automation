#!/bin/env python


import sys
import json
from datetime import datetime

def timestamp():
# ->| return two date formats
    Y = datetime.now().year
    M = format( datetime.now().month, "02d" )
    D = format( datetime.now().day, "02d" )
    h = format( datetime.now().hour, "02d" )
    m = format( datetime.now().minute, "02d" )
    s = format( datetime.now().second, "02d" )

    dstamp = ( str( Y ) +'-'+ str( M ) +'-'+ str ( D ))
    tstamp = ( str( h ) + str( m ) + str ( s ))
    return([ dstamp,tstamp ])



filename = timestamp()[0] + '-webrtc_parse-' + timestamp()[1] + '.csv'

f = open( sys.argv[1], 'r' )
with open( filename, 'w' ) as file:
    pass

jdata = json.loads( f.read() )
k2 = list( jdata['PeerConnections'].keys())

#
for i in k2:
    data = jdata['PeerConnections'][ i ]['stats']
    for x in data.keys():
        v = []
        v.append( x )
        y = jdata['PeerConnections'][ i ]['stats'][ x ]['values'].split(',')

# ----->| for each item in row
        for z in range( 0, len( y ) - 1 ):

# --------->| if items are strings, strip quotes and append once
            if '"' in y[z]:
                e = str( y[z].strip( '[\"' ))
                if ' ' in e:
                    e = str( e.split( ' ' )[0] )
                if len( e ) > 20:
                    e = e[:20]
                v.append( e )
                break
# --------->| if list items are int or float, format
            else:
                try:
                    e = format( float( y[z + 1] ), ".1f" )
                    v.append( str( e ))
                except:
                    pass

                try:
                    e = int( y[z + 1] )
                    v.append( str( e ))
                except:
                    pass

# ----->|
        if len( v ) > 1:
            v2csv = ','.join( v )
            print( v2csv )
            with open( filename,'a' ) as file:
                file.write( v2csv + "\n" )
            file.close()
        if len( v ) < 2:
            pass
        v = []

