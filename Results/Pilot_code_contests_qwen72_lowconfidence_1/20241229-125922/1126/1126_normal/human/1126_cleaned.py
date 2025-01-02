input = sys.stdin
output = sys.stdout
"\ninput = open('input.txt','r')\noutput = open('output.txt','w')\n"
input.readline()
woods = map(lambda x: int(x), input.readline().strip().split(' '))
d = {}
for w in woods:
    d[w] = d.setdefault(w, 0) + 1
output.write('%d %d' % (max(d.values()), len(d)))
output.close()