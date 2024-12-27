import sys

pattern = 'heidi'
text = sys.stdin.readline()

match = False
max_match = 0
for char in text:
	if char == pattern[max_match]:
		max_match += 1
	if max_match == len(pattern):
		match = True
		break

print('YES' if match else 'NO')