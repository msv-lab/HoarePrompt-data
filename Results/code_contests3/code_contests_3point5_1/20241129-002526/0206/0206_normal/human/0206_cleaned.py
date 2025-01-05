N = raw_input()
a = raw_input().split()
ans = np.abs(np.max(a) - np.min(a))
print(ans)