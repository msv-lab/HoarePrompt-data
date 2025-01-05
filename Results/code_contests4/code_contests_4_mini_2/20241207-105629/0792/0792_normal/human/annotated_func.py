#State of the program right berfore the function call: n is a positive integer such that 3 ≤ n ≤ 105, and a is a list of n positive integers where each element ai satisfies 1 ≤ ai ≤ 10^9.
def func():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a = sorted(a)
    x = a[2]
    ans = 1
    for i in xrange(3, len(a)):
        if a[i] == x:
            ans += 1
        else:
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 3, `x` is the third smallest number in the list `a`, and `ans` is the count of occurrences of `x` in `a` starting from index 3, including the initial value of 1 if no occurrences were found.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` positive integers. It sorts the list and identifies the third smallest number, `x`. It then counts how many times `x` appears in the list starting from the fourth position (index 3), returning this count. If `x` does not appear in the list after the third position, it returns 1. However, the function does not handle cases where `n` is less than 3 or if the input is invalid. Additionally, the function does not return any value but instead prints the count.

