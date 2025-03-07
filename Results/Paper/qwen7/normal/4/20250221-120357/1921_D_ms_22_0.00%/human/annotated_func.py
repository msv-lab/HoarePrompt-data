#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are lists of integers where 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
            
        #State: After all iterations of the loop, `max_heap` will be empty, indicating that all items have been processed. The variable `ans` will hold the sum of the negative differences calculated during each iteration of the loop. Specifically, for each item popped from `max_heap`, the code updates `ans` by adding either the negative value of the first element of the popped item, the absolute difference between `item[1]` and `b[tp1]` if `diff1` is greater than `diff2`, or the absolute difference between `item[1]` and `b[tp2]` if `diff2` is greater than or equal to `diff1`. Additionally, `tp1` will be incremented by 1 if `item[2]` is less than `tp1`, and `tp2` will be decremented by 1 if `item[2]` is greater than `tp2`. Otherwise, `ans` is increased by the greater of `diff1` and `diff2`.
    #State: `max_heap` will be empty, indicating that all items have been processed. The variable `ans` will hold the sum of the negative differences calculated during each iteration of the loop. Specifically, for each item popped from `max_heap`, `ans` is updated by adding either the negative value of the first element of the popped item, the absolute difference between `item[1]` and `b[tp1]` if the difference is greater than the absolute difference between `item[1]` and `b[tp2]`, or the absolute difference between `item[1]` and `b[tp2]` if the difference is greater than or equal to the previous difference. Additionally, `tp1` will be incremented by 1 if `item[2]` is less than `tp1`, and `tp2` will be decremented by 1 if `item[2]` is greater than `tp2`. Otherwise, `ans` is increased by the greater of the two differences.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two integers \( n \) and \( m \), and two lists of integers \( a_i \) and \( b_i \). It sorts the list \( b \) and then calculates the sum of the minimum absolute differences between elements of \( a_i \) and the closest elements in \( b \). Specifically, for each element in \( a_i \), it finds the closest element in \( b \) and adds the absolute difference to the total sum. The function returns the total sum of these differences for all test cases.

