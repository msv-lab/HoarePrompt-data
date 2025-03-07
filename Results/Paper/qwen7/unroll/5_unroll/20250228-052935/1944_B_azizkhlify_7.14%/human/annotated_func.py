#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The list a is a list of 2n integers where each integer from 1 to n appears exactly twice.
def func():
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        
        a = [int(i) for i in input().split()]
        
        l = [0] * n
        
        r = [0] * n
        
        re = ul = ur = 0
        
        res = []
        
        for i in range(n):
            l[a[i] - 1] += 1
        
        for i in range(n, 2 * n):
            r[a[i] - 1] += 1
        
        for i in range(n):
            if l[a[i] - 1] == 2:
                print(a[i], a[i], end=' ')
                ul += 2
            if ul == k * 2:
                break
        
        k = 2 * k - ul
        
        if k:
            for i in range(n):
                if l[a[i] - 1] == 1:
                    print(a[i], end=' ')
                    re += 1
                    res.append(a[i])
                if re == k:
                    break
        
        print()
        
        for i in res:
            print(i, end=' ')
        
        if ul != ur:
            for i in range(n, 2 * n):
                if r[a[i] - 1] == 2:
                    print(a[i], a[i], end=' ')
                    ur += 2
                if ul == ur:
                    break
        
        print()
        
    #State: Output State: The output consists of multiple lines, each corresponding to a test case. For each test case, it prints pairs of numbers from the list `a` based on the following rules:
    #
    #1. It first prints pairs of numbers from the first half of the list `a` (indices 0 to n-1) where each number appears exactly twice. It stops once it has printed `k` such pairs or when there are no more such pairs left.
    #2. If there are still required pairs (`k` is not zero), it then prints single occurrences from the first half of the list `a` until it has printed the remaining required pairs.
    #3. After that, it prints the collected single occurrences from step 2.
    #4. Finally, it prints pairs of numbers from the second half of the list `a` (indices n to 2n-1) where each number appears exactly twice, stopping when it matches the count of pairs printed in the first step.
    #
    #Each line ends with a space-separated list of the single occurrences printed during the process, followed by a newline.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice, along with two integers n and k. It prints pairs of numbers from the first half of the list and single occurrences from the first half based on the value of k. After that, it prints the collected single occurrences and finally pairs from the second half of the list, ensuring the total number of printed pairs and single occurrences matches the specified k. The function does not return any value but outputs the results directly.

