#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200000, and the sequence of doors opened is a list of integers where each integer is either 0 (for left exit) or 1 (for right exit). There is at least one 0 and at least one 1 in the sequence.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `ans` is the index of the last differing element plus one or 0 if all elements are equal, `c` is a map object of integers from the input list.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (the number of doors) and a list `c` of integers (0 or 1 indicating left or right exits), and prints the index (plus one) of the last differing door or 0 if all doors are the same. It does not return "left" or "right" as incorrectly stated in the annotations.

