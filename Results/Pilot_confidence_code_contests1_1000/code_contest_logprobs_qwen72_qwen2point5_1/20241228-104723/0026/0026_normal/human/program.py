import sys

victims = sys.stdin.readline().strip().split()
days = int(sys.stdin.readline().strip())

for day in range(days):
  print(victims[0] + ' ' + victims[1])
  newPeople = sys.stdin.readline().strip().split()
  killed = newPeople[0]
  replacer = newPeople[1]

  if victims[0] == killed:
    victims[0] = replacer
  elif victims[1] == killed:
    victims[1] = replacer

print(victims[0] + ' ' + victims[1])
