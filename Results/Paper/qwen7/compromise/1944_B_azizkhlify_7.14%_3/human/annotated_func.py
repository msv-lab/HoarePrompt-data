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
        
    #State: Output State: The output state after the loop executes all the iterations is a string formed by concatenating the values of `a[0]`, `a[3]`, and `a[5]` from the array `a`.
    #
    #To understand this output state, let's break down the logic of the loop:
    #
    #1. **Initialization and Input Handling:**
    #   - The loop processes multiple test cases, each with its own values of `n`, `k`, and the list `a`.
    #   - `l` and `r` arrays keep track of the occurrences of each number in the first half and second half of the list `a`, respectively.
    #   - `res` is a list used to store results during the processing of each test case.
    #
    #2. **First Pass (Left Half):**
    #   - For each number in the first half of `a`, it increments the corresponding index in the `l` array.
    #   - It checks if any number has appeared twice in the left half (`l[a[i] - 1] == 2`). If so, it prints these numbers twice and increments `ul` by 2.
    #   - It breaks the loop if `ul` reaches `k * 2`.
    #
    #3. **Adjusting `k`:**
    #   - After the first pass, it adjusts `k` to `2 * k - ul`.
    #
    #4. **Second Pass (Right Half):**
    #   - For each number in the right half of `a`, it increments the corresponding index in the `r` array.
    #   - It checks if any number has appeared once in the left half (`l[a[i] - 1] == 1`). If so, it prints these numbers once and increments `re` by 1.
    #   - It breaks the loop if `re` reaches `k`.
    #   - It then prints the contents of `res`.
    #
    #5. **Third Pass (Right Half Again):**
    #   - If `ul` does not equal `ur`, it processes the right half again, printing pairs of numbers that have appeared twice in the right half until `ul` equals `ur`.
    #
    #6. **Final State:**
    #   - After all iterations, the final state of the loop ensures that `i` is `2 * n`, indicating the loop has processed all elements.
    #   - `n` must be greater than 0, as it represents the number of unique elements in the list `a`.
    #   - `ur` retains its original value, meaning the number of pairs found in the right half remains consistent.
    #
    #Given the structure of the loop and the specified conditions, the final output is determined by the specific values of `a[0]`, `a[3]`, and `a[5]` after all iterations. Therefore, the output state is a string formed by concatenating these values.
#Overall this is what the function does:The function processes a list of 2n integers (a) for each test case, where n is an integer between 2 and 50,000, and k is an integer between 1 and n/2. Each integer from 1 to n appears exactly twice in the list a. The function prints specific pairs of numbers based on the occurrences of these numbers in the list, and finally outputs a string formed by concatenating the values of `a[0]`, `a[3]`, and `a[5]` from the array `a`.

