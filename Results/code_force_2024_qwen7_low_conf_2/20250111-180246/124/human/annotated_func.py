#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^2, and for each test case, n is an integer such that 3 ≤ n ≤ 3 \cdot 10^4. Additionally, the sum of n over all test cases does not exceed 3 \cdot 10^4.
def func_1():
    input = sys.stdin.read
    data = input().split()
    ans1 = [8]
    ans2 = [[[2, 6, 8], [3, 5, 7]]]
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        if n in ans1:
            ans = ans2[ans1.index(n)]
            results.append(f'{len(ans)}')
            for x in ans:
                results.append(' '.join(map(str, x)))
            continue
        
        ans = []
        
        pos = 0
        
        ost = []
        
        for i in range(3, n - 1, 4):
            if i > n // 2 - 2:
                ans.append([i, i + 1, i + 2])
                pos = i + 2
        
        for i in range(pos + 1, n + 1):
            if (i % 2 != 0 or i % 4 == 0) and i > n // 2:
                ost.append(i)
        
        per = n
        
        if (n - 1) % 4 == 2:
            per = n - 1
        elif (n - 2) % 4 == 2:
            per = n - 2
        elif (n - 3) % 4 == 2:
            per = n - 3
        
        for i in range(per, n // 2, -12):
            if i > n // 2:
                if i > 8:
                    ans.append([i, i - 4, i - 8])
                else:
                    ost.append(i)
        
        if len(ost) == 1:
            ans.append([1, 2, ost[0]])
        elif len(ost) == 2:
            ans.append([1, ost[1], ost[0]])
        elif len(ost) == 3:
            ans.append([ost[0], ost[1], ost[2]])
        elif len(ost) == 4:
            ans.append([1, ost[0], ost[1]])
            ans.append([2, ost[2], ost[3]])
        
        results.append(f'{len(ans)}')
        
        for x in ans:
            results.append(' '.join(map(str, x)))
        
    #State of the program after the  for loop has been executed: `ans` is a list of valid triplets generated based on the values of `n` in `data`, `per` and `pos` retain their last computed values, `results` is a list containing the number of valid triplets followed by the triplets themselves.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases where each test case involves an integer \(n\) such that \(3 \leq n \leq 3 \cdot 10^4\). For each \(n\), the function generates valid triplets based on certain conditions and appends these triplets to a result list. If \(n\) is found in a predefined list `ans1`, it retrieves precomputed triplets from `ans2`. Otherwise, it computes the triplets according to specific rules involving arithmetic progressions and modulo operations. The function then outputs the number of generated triplets followed by the triplets themselves, formatted as a series of lines in the standard output. The function handles edge cases where \(n\) might not fit into the predefined list and ensures that the output adheres to the constraints specified.

