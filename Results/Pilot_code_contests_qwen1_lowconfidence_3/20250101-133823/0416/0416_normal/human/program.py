n = int(raw_input())
line = raw_input()

change_red = 0
change_black = 0
for idx,val in enumerate(line):
	if idx%2 == 0 and val == 'b':
		change_black += 1
	if idx%2 == 1 and val == 'r':
		change_red += 1
swaps = min(change_red, change_black)
color = max(change_red, change_black) - swaps

total = swaps + color

change_red2 = 0
change_black2 = 0
for idx,val in enumerate(line):
	if idx%2 == 1 and val == 'b':
		change_black2 += 1
	if idx%2 == 0 and val == 'r':
		change_red2 += 1


swaps2 = min(change_red2, change_black2)
color2 = max(change_red2, change_black2) - swaps2

total2 = swaps2 + color2

print(min(total, total2))



