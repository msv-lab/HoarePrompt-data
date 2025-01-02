from heapq import *
input = __import__("sys").stdin.readline
n, k = map(int, input().split())
seg = []
events = []
remove = __import__("collections").defaultdict(int)
for _ in xrange(n):
	l, r = map(int, input().split())
	seg.append((l, r))
	events.append((l, True, r))
	events.append((r + 1, False, None))
events.sort(reverse=True)
cover = 0
heap = []  # (-end, start)
rem = 0
post = __import__("collections").defaultdict(int)
while events:
	ind, add, release = events.pop()
	if add:
		cover += 1
		heappush(heap, (-release, ind))
	elif post[ind]:
		post[ind] -= 1
	else:
		cover -= 1
	while events and events[-1][0] == ind:
		ind, add, release = events.pop()
		if add:
			cover += 1
			heappush(heap, (-release, ind))
		elif post[ind]:
			post[ind] -= 1
		else:
			cover -= 1
	while cover > k:
		end, start = heappop(heap)
		end = -end
		post[end + 1] += 1
		remove[(start, end)] += 1
		rem += 1
		cover -= 1
print(rem)
for i in xrange(len(seg)):
	if remove[seg[i]]:
		print(i + 1),
		remove[seg[i]] -= 1
print