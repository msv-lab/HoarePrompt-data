from sys import stdin, stdout
ti = lambda : stdin.readline().strip()
ma = lambda fxn, ti : map(fxn, ti.split())
ol = lambda arr : stdout.write(' '.join(str(i) for i in arr) + '\n')
os = lambda i : stdout.write(str(i) + '\n')
olws = lambda arr : stdout.write(''.join(str(i) for i in arr) + '\n')


n = int(ti())
a = ma(int, ti())
freq = [0] * (10**5+1)
for i in range(n):
	freq[a[i]] += 1

# print freq
dp = [0, freq[1]]
for i in range(2, n+1):
	# print i, dp
	dp.append(max(dp[i-1], dp[i-2] + freq[i]*i))

os(dp[n])