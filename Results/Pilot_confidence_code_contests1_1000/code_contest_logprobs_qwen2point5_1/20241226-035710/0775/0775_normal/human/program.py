def count(arr,cnt):
	for i in range(0,len(arr)):
		if arr[i] in cnt.keys():
			cnt[arr[i]] = cnt[arr[i]] + 1
		else:
			cnt[arr[i]] = 1
def yn2048(arr,t):
	f = {}
	count(arr,f)
	keys = f.keys()
	for i in range(0,11):
		k = 0
		if pow(2,i) in keys:
			 k = f[pow(2,i)]/2 
		if pow(2,i+1) in keys:
			f[pow(2,i+1)] = f[pow(2,i+1)] + k
		elif k > 0:
			f[pow(2,i+1)] = k
	if 2048 in f:
		t.append("YES")
	else:
		t.append("No")

def main():
	t = []
	q = int(raw_input())
	for i in range(q):
		f = raw_input()
		arr = list(map(int,raw_input().split(" ")))
		yn2048(arr,t)
	for i in t:
		print (i)
main()	
