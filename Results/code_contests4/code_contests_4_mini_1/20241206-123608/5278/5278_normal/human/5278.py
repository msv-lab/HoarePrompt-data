n, k = [ int( val ) for val in raw_input( ).split( " " ) ]
w = []
maxW = sumW = 0
for i in range( n ):
	num = int( raw_input( ) )
	sumW += num
	w.append( num )
	if maxW < num:
		maxW = num

minP = 0
if 1 == k:
	minP = sumW
elif n == k:
	minP = maxW
else:
	left = maxW
	right = 100000*10000
	while left <= right:
		middle = ( left+right )//2
		truckCnt = i = loadings = 0
		while i < n:
			loadings += w[i]
			if middle < loadings:
				truckCnt += 1
				if k < truckCnt+1:
					break
				loadings = w[i]
			i += 1

		if truckCnt+1 <= k:
			minP = middle
		
		if k < truckCnt+1:
			left = middle + 1
		else:
			right = middle - 1