cards = input()
tablets = cards.count('T')
compasses = cards.count('C')
gears = cards.count('G')

points = (tablets ** 2) + (compasses ** 2) + (gears ** 2)
points += 7 * min(tablets, compasses, gears)

print(points)