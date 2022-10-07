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
with open( filename, 'w' ) as file:
    pass

f = open( sys.argv[1], 'r' )
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

# --------->| if items are strings, clean up and append first value
            if '"' in y[z]:
                e = str( y[z] )
                e = e.strip( '\"' )
                e = e.strip( '[\"' )
                if ' ' in e:
                    e = str( e.split( ' ' )[0] )
                if len( e ) > 20:
                    e = e[:20]
                v.append( e )
                break

# --------->| if list items are int or float, format floats
            else:
                try: e = format( float( y[z + 1] ), ".1f" )
                except: pass

                try: e = int( y[z + 1] )
                except: pass

                v.append( str( e ))

# ----->| average values into second column

        if len( v ) > 3:
            total = 0
            average = len( v[1:] )
            for x in v[1:]:
                try:
                    total = total + float( x )
                except:
                    pass
            avg = format( float( total / average ), ".1f" )
            v.insert( 1,str( avg ))

# ----->| convert list to csv for write and print
        if len( v ) > 1:
            v2csv = ','.join( v )
            print( v2csv )
            with open( filename,'a' ) as file:
                file.write( v2csv + "\n" )
            file.close()
# ----->| do not write if no values in row
        if len( v ) < 2:
            pass
        v = []

