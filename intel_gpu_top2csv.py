#!/usr/bin/python
# -*- coding: utf-8 -*-
# intel_gpu_top v0.0

# ---
# parse output from intel_gpu_top -l,
# calculating out an average row as the last line, and
# output to new csv.
#
# HOW TO USE:
# add folders to script directory and run `python intel_gpu_top.txt`
# ---

import os

def paths():

# ->| assign values
    my_dir = '.'
    file_suffix = '--intel_gpu_top.txt'
    output = '--intel_gpu_top.csv'

# ->| list all directories ending with file_suffix
    b = []
    for d in os.listdir( my_dir ):
            if d.endswith( file_suffix ):
                b.append( d )

# ->| for each directory listed in b[]
    for d in b:

# ----->| loop through file one line at a time

        print( d ) # debug
        f = os.path.join( my_dir,d )
        file = open( f,'r' )

        h1 = "Freq (req),MHz (act),IRQ /s,RC6 %,RCS/0 %,RCS/0 se,RCS/0 wa,BCS/0 %,BCS/0 se,BCS/0 wa,"
        h2 = "VCS/0 %,VCS/0 se,VCS/0 wa,VCS/1 %,VCS/1 se,VCS/1 wa,VECS/0 %,VECS/0 se,VECS/0 wa"
        header = h1 + h2
        print( header ) # debug

        x = 0
        row = []
        r = []

# ----->| limit size of rows ( ex: 19 rows )
        while len( row ) < 19:
            next_line = file.readline()
            if not next_line:
                break
            if next_line[1].isalpha():
                pass
            else:
                line = next_line.strip()
                line = line.replace( ' ',',' )
                while ',,' in line:
                    line = line.replace( ',,',',' )

                csv = line.strip().split(',')
                for i in csv:
                    r.append( i )

                x = x + 1
                row.append( r )
                r = []
# ----->|
        file.close()
        #print( row ); print( row[0] ) # debug

# ----->| relist and append average at end of each list ( optional )
        x = len( row[0] )
        z = 0
        c = []
        while z < x:
            m = []
            for i in row:
                m.append( i[z] )
            length = len( m )
            total = 0
            for i in m:
                total = total + float( i )
                avg = total / length
            average = format( avg, ".2f" )
            m.append( average )
            z = z + 1
            c.append( m )

        # print( c ) # debug
# ----->| reorient rows to original format
        x = len( c[0] )
        z = 0
        e = []
        while z < x:
            m = []
            for i in c:
                m.append( i[z] )
            z = z + 1
            e.append( m )

            with open( 'myfile.csv','w' ) as my_output:
                for i in e:
                    for o in i:
                        my_output.write( str( o ) + ',' )
                    my_output.write( '\n' )
#                    #print( i,end=',' )
#                    v = ( ','.join( i ))
#                    print( v )
#                    #my_output.write( i )
#            print( "",end='\n' )

        print( e ) # debug
# ----->|
#        out = open( 'myfile.csv', 'w' )
#        for i in e:
#            out.write( '"' + '","'.join(row) + '"\n' )

if __name__ == "__main__":
    paths()

