#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. The list a contains n integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise different. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: The loop will execute until it finds an element `a[i]` that is greater than `a[k-1]` or until it has checked all elements. If it checks all elements without finding one greater than `a[k-1]`, `i` will be `n` and `wins` will be `n`. If it breaks early, `i` will be the index where the condition `a[i] > a[k-1]` is met, and `wins` will be the number of elements checked before breaking.
    #
    #In natural language:
    #- The variable `i` will be the index where the loop broke (i.e., the first index `i` such that `a[i] > a[k-1]`), or `n` if no such index exists.
    #- The variable `wins` will be the number of elements in `a` up to index `i-1` that are less than or equal to `a[k-1]`, or `n` if all elements are less than or equal to `a[k-1]`.
    #
    #Output State:
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements checked before breaking the loop or `n` if the loop checks all elements)
        return
        #The program returns nothing (None)
    #State: The loop will execute until it finds an element `a[i]` that is greater than `a[k-1]` or until it has checked all elements. If it checks all elements without finding one greater than `a[k-1]`, `i` will be `n` and `wins` will be `n`. If it breaks early, `i` will be the index where the condition `a[i] > a[k-1]` is met, and `wins` will be the number of elements checked before breaking. Additionally, `wins` will be less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `win_with_swap` is `k` and `i` is `k-1`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, k - wins) if wins != 0, otherwise k - 1 (where wins is an unknown integer and k is the value of win_with_swap)
#Overall this is what the function does:The function reads two integers `n` and `k`, and a list of `n` integers. It then determines the number of elements in the list that are less than or equal to the element at index `k-1` (1-based index). If this count is at least `k`, it prints `wins - 1`. Otherwise, it calculates the maximum of `wins - 1` and the number of additional elements that can be included in the top `k` by potentially swapping the element at index `k-1` with a larger element later in the list, and prints this value. The function does not return any value.

