#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3, and a_1, a_2, ..., a_n are integers such that 0 ≤ a_i < 300.
def func():
    n = int(input())

a = list(map(int, input().split()))
    while len(a) > 1:
        if min(a) == 0:
            a.remove(0)
        else:
            x = min(a)
            a = [(i - x) for i in a]
        
    #State of the program after the loop has been executed: `n` is either 2 or 3, and the length of list `a` is 1. Each element in list `a` is non-negative and less than 300, and the minimum value of `a` is 0.
    if a :
        print('BitLGM' if a[0] % 2 == 0 else 'BitAryo')
    else :
        print('BitAryo')
    #State of the program after the if-else block has been executed: *`n` is either 2 or 3, and the length of list `a` is 1. Each element in list `a` is non-negative and less than 300, and the minimum value of `a` is 0. If `a` is not an empty list, the program does not change the state of `a` or print anything. If `a` is an empty list or all elements in `a` are truthy (non-zero), 'BitAryo' is printed to the console.
#Overall this is what the function does:The function accepts a list of integers `a` where the length of the list `n` is between 1 and 3 (inclusive), and each integer in the list satisfies \(0 \leq a_i < 300\). It then removes all zeros from the list and adjusts the remaining elements by subtracting the minimum non-zero value, ensuring that the list contains at most one element. After processing, the function prints 'BitLGM' if the single remaining element (if any) is even, and 'BitAryo' otherwise. If the list becomes empty during the process, it prints 'BitAryo'.

