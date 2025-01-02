import sys
from sys import stdin , stdout

def getInput() :
    sys.stdin.readline()
    return [ int( x ) for x in sys.stdin.readline().split() ]

def setOutput( ns ) :
    for el in ns :
        sys.stdout.write( str( el ) + '\n')

def jumps( maxim , minim ) :
    jump = 1 ;
    while ( jump < minim ) :
        jump *= 2
    if ( jump > maxim ) :
        jump /= 2
    res = 1
    while ( minim > jump ) :
        maxim -= jump
        minim -= jump
        while ( jump > maxim ) :
            jump /= 2
        res += 1
    return res


def solve( inp ) :
    res = []
    total = 0
    for k in range( 1 , len( inp ) ) :
        total = 0
        for i in range( k ) :
            total += inp[ i ] * jumps( ( len( inp ) - i - 1 ) , ( k - i ) )
        res.append( total )
    return res



def main():
    setOutput( solve( getInput() ) )

if __name__ == '__main__':
    main()
