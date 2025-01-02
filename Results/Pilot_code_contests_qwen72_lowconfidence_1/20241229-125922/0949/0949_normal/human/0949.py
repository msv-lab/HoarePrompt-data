from itertools import chain

n = int(raw_input())
a = list(sorted(map(int,raw_input().split())))

team = set()

for boxer in a :
    if boxer - 1 > 0 and boxer - 1 <= 150001 and boxer - 1 not in team :
    	team.add(boxer - 1)
    elif boxer > 0 and boxer <= 150001 and boxer not in team :
    	team.add(boxer)
    elif boxer + 1 > 0 and boxer + 1 <= 150001 and boxer + 1 not in team :
    	team.add(boxer + 1)

print(len(team),team)

#print(min(
#	n, len(
#		set(
#			list(
#				filter(lambda x : 0<x<=150001,
#					chain.from_iterable([[i-1,i,i+1] for i in a])
#					)
#				)
#			)
#		)
#	)
#)
