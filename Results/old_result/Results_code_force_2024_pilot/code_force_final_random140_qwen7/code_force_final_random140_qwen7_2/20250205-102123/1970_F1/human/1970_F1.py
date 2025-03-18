from sys import stdin
 
mov = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1),'T':(0,0)};
GoalName = ["RED", "BLUE"]
 
def main():
    n,m = map(int,stdin.readline().strip().split());
    grid = [];
    elements = {".B":(0,0)};
    allPlayers = {};
    goal = [[],[]]
    points= [0,0];
    
    def goalIn( pos ):
        res = 0 if ( pos in goal[0] ) else ( 1 if ( pos in goal[1] ) else -1 );
        return res;
    def isPlayer( el ):
        res = (el[0] == 'B' or el[0] == 'R')and(el[1]!='G');
        return res;
    
    for i in range(n):
        line = stdin.readline().strip().split();
        grid.append( line );
        for ind in range(len(line)):
            if ( line[ind] != ".." ):
                elements[line[ind]] = (i,ind);
                if ( isPlayer( line[ind] ) ):
                    allPlayers[line[ind]] = False;
                elif ( line[ind][1]=='G' ):
                    tmp = 0 if line[ind][0] =='B' else 1;
                    goal[tmp].append( (i,ind) );
    
    t = int(stdin.readline().strip());
    for time in range( t ):
        comand = stdin.readline().strip().split();
        if ( len(comand) == 3 ):
            obj, com, el = comand;
            if ( el == ".Q" ):
                # print("lo agarra en (%d, %d)" % ( elements[obj][0], elements[obj][1] ) );
                allPlayers[obj] = True;
            elif ( el == ".S" ):
                team = 1 if obj[0] =='B' else 0;
                points[team] += 10;
                print( "%d %s CATCH GOLDEN SNITCH" % ( time, GoalName[team] ) );
        else:
            obj, com = comand;
            pos = elements[obj];
            nxt = (pos[0]+mov[com][0], pos[1]+mov[com][1] );
            if ( ( obj == ".B" and isPlayer(grid[nxt[0]][nxt[1]]) ) or ( isPlayer(obj) and elements[".B"]==nxt ) ):
                player =  obj if isPlayer(obj) else grid[nxt[0]][nxt[1]];
                print( "%d %s ELIMINATED" % (time, player ) );
            elif ( com=='T' ):
                allPlayers[obj] = False;
                if ( goalIn(pos)!=-1 ):
                    team=goalIn(pos);
                    print( "%d %s GOAL" %( time, GoalName[team] ) );
                    points[team] += 1;
            elif( isPlayer(obj) ):
                elements[obj] = nxt;
            
            if ( obj == ".B" ):
                elements[obj] = nxt;
            
    print("FINAL SCORE: %d %d"%( points[0], points[1] ));
                
                
                
 
main();