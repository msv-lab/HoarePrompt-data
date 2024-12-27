import sys

def getArgs():
  args = []
  for line in sys.stdin:
    args.append(line)
  return args

def shortenWord(word):
  n = len(word) - 2
  return word[0] + str(n) + word[n+1]

argLines = getArgs()

n = int(argLines[0])
argLines.pop(0)
for word in argLines:
  w = word.replace('\n', '')
  if(len(w) > 10):
    print(shortenWord(w))
  else:
    print(w)
