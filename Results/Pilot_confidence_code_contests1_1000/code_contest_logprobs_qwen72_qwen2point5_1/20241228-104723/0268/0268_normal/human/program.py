def inc(s, freq, k, i):
	if i == len(s):
		return False

	freq[ord(s[i]) - ord('a')] += 1

	if inc(s, freq, k, i+1):
		return s

	freq[ord(s[i]) - ord('a')] -= 1	

	if s[i] == 'z':
		return False
	else:
		
		for c in range(ord(s[i]) + 1, ord('z') + 1):

			freq[c-ord('a')] += 1

			mand = 0
			for j in range(26):
				if freq[j] % k != 0:
					mand += (k - freq[j]%k)

			left = n-i-1

			if left < mand or (left-mand) % k != 0:
				freq[c-ord('a')] -= 1
				continue

			else:
				s[i] = chr(c)
				remain = []
				for j in range(26):
					if freq[j] % k != 0:
						remain += [chr(ord('a') + j)] * (k - freq[j]%k)

				if mand < left:
					remain += ['a'] * (left - mand)

				remain.sort()

				s[i+1:] = remain

				return True

		return False
		


for _ in range(input()):
	n, k = map(int, raw_input().split())
	s = list(raw_input())

	freq = [0] * 26

	if inc(s, freq, k, 0):
		print(''.join(s))
	else:
		print(-1)

