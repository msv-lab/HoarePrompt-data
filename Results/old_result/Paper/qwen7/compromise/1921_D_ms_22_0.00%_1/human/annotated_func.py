#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are positive integers such that 1 ≤ n ≤ m ≤ 2 ⋅ 10^5 and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
            
        #State: After all iterations of the loop, `max_heap` is empty, indicating that all items have been processed. The variable `ans` holds the total minimum sum of absolute differences between the elements of list `a` and the boundary elements of list `b` (either the first or the last element). The variables `tp1` and `tp2` are adjusted to cover the entire range of indices in `b` based on the conditions specified in the loop body.
    #State: `max_heap` is empty, indicating that all items have been processed. The variable `ans` holds the total minimum sum of absolute differences between the elements of list `a` and the boundary elements of list `b` (either the first or the last element). The variables `tp1` and `tp2` are adjusted to cover the entire range of indices in `b` based on the conditions specified in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, m, a_i, and b_i. It sorts the list b and then calculates the minimum sum of absolute differences between each a_i and either the smallest or largest element in the sorted list b. The function returns the total minimum sum of these differences for each test case.

