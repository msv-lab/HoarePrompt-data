import fileinput
import math

for line in fileinput.input():
    attendees = int(line.strip())
    min_brains = math.ceil(attendees / 2)
    min_brains = max(1, min_brains)
    print(min_brains)
    