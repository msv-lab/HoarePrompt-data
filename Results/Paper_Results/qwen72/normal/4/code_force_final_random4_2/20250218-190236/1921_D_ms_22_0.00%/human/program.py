import math
import heapq
 
if __name__ == "__main__":
    t  = int(input())
    while t > 0:
        t -= 1
        
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        b.sort()
        
        max_heap = []
        
        tp1 = 0
        tp2 = m-1
        
        ans = 0
        
        for i in a : 
            diff1 = abs(i - b[0])
            diff2 = abs(i - b[m-1])
            if diff1 > diff2:
                heapq.heappush(max_heap, (-diff1, i, 0))
            else:
                heapq.heappush(max_heap, (-diff2, i , m-1))
        
        while max_heap:
            item = heapq.heappop(max_heap)
            if item[2] < tp1 or item[2] > tp2:
                diff1 = abs(item[1] - b[tp1])
                diff2 = abs(item[1] - b[tp2])
                if diff1 > diff2:
                    tp1 += 1
                    ans += diff1
                    #heapq.heappush(max_heap, (-diff1, item[1], tp1))
                else:
                    tp2 -= 1
                    ans += diff2
                    #heapq.heappush(max_heap, (-diff2, item[1] , tp2))
            
            else:
                ans += (-item[0])
                if item[2] == tp1:
                    tp1 += 1
                else:
                    tp2 -= 1
                    
        print(ans)