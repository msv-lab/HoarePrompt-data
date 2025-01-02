VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

# main
n = int(raw_input())
p = [int(x) for x in raw_input().split()]

answer = True
for pi in p:
	line = raw_input()
	syllables = sum([c in VOWELS for c in line])
	answer = answer and (syllables == pi)

print ('YES' if answer else 'NO')