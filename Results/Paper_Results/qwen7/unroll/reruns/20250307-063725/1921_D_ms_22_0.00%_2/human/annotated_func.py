#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            n, m = map(int, input().split())
            
            a = list(map(int, input().split()))
            
            b = list(map(int, input().split()))
            
            b.sort()
            
            max_heap = []
            
            tp1 = 0
            
            tp2 = m - 1
            
            ans = 0
            
            for i in a:
                diff1 = abs(i - b[0])
                diff2 = abs(i - b[m - 1])
                if diff1 > diff2:
                    heapq.heappush(max_heap, (-diff1, i, 0))
                else:
                    heapq.heappush(max_heap, (-diff2, i, m - 1))
            
            while max_heap:
                item = heapq.heappop(max_heap)
                if item[2] < tp1 or item[2] > tp2:
                    diff1 = abs(item[1] - b[tp1])
                    diff2 = abs(item[1] - b[tp2])
                    if diff1 > diff2:
                        tp1 += 1
                        ans += diff1
                    else:
                        tp2 -= 1
                        ans += diff2
                else:
                    ans += -item[0]
                    if item[2] == tp1:
                        tp1 += 1
                    else:
                        tp2 -= 1
            
            print(ans)
            
        #State: The value of `t` is 0, and the variable `ans` contains the sum of minimum absolute differences between elements of array `a` and a subset of array `b` (of size `m`) after sorting and processing as described in the loop.
    #State: `t` is a positive integer such that 1 ≤ t ≤ 100. If `t` is 0, the variable `ans` contains the sum of minimum absolute differences between elements of array `a` and a subset of array `b` (of size `m`) after sorting and processing as described in the loop. Otherwise, no change is made to `t` and `ans` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes integers t, n, m, a_i, and b_i. It calculates and returns the sum of the minimum absolute differences between elements of array a and a sorted subset of array b (of size m). The function ensures that t is a positive integer within the range 1 to 100, and for each test case, n and m are integers within the specified ranges, with n ≤ m, and the sum of m across all test cases does not exceed 2 * 10^5. Additionally, a_i and b_i are integers within the range 1 to 10^9.

