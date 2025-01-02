#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100,000, x and y are integers such that 0 ≤ x, y ≤ 7, and a is a list of n distinct integers where 1 ≤ a_i ≤ 10^9.
def func():
    sys.setrecursionlimit(10 ** 6)
    n, x, y = map(int, raw_input().split())
    inp2 = map(int, raw_input().split())
    for i in range(n):
        flag = True
        
        val = inp2[i]
        
        for bef in range(1, x + 1):
            indis = i - bef
            if indis < 0:
                break
            if indis >= n:
                break
            if val > inp2[indis]:
                flag = False
                break
        
        for aft in range(1, y + 1):
            indis = i + aft
            if indis < 0:
                break
            if indis >= n:
                break
            if val > inp2[indis]:
                flag = False
                break
        
        if flag:
            print(i + 1)
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer from the input such that 1 ≤ n ≤ 100,000, `x` is an integer from the input such that 0 ≤ x ≤ 7, `y` is an integer from the input such that 0 ≤ y ≤ 7, `a` is a list of n distinct integers where 1 ≤ a_i ≤ 10^9, the recursion limit is set to 1,000,000, `inp2` is a list (or iterator) of integers obtained from the input, `i` is the last index of `inp2` checked, `val` is the last element of `inp2` that was processed, `aft` is the last value of `aft` before the loop terminated, `indis` is the last value of `indis` before the loop terminated. If the loop completes without breaking, `i` will be `n-1`. If the loop finds an `i` such that `val` (which is `inp2[i]`) is not greater than any element in `inp2` from `i - x` to `i + y` (inclusive), `flag` remains `True`, and `i + 1` is printed. If no such `i` is found, the loop completes without printing anything, and `flag` is `False`.
#Overall this is what the function does:The function reads two lines of input. The first line contains three integers `n`, `x`, and `y`, where `1 ≤ n ≤ 100,000` and `0 ≤ x, y ≤ 7`. The second line contains `n` distinct integers, each between `1` and `10^9`. The function then checks each element in the list to see if it is not greater than any of its `x` preceding elements or `y` following elements. If such an element is found, the function prints the 1-based index of this element and terminates. If no such element is found, the function completes without printing anything. The recursion limit is set to 1,000,000, but the function does not use recursion. The final state of the program includes the updated recursion limit and the processed input variables, but the original list `a` is not modified.

