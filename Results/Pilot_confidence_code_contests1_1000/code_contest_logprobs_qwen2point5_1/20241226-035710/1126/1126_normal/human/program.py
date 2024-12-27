import sys
input = sys.stdin
output = sys.stdout
'''
input = open('input.txt','r')
output = open('output.txt','w')
'''

input.readline()
woods = map(lambda x: int(x), input.readline().strip().split(' '))

d = {}
for w in woods:
  d[w] = d.setdefault(w,0) + 1
  
output.write('%d %d'%(max(d.values()), len(d)))
output.close()

