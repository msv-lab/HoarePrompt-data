#State of the program right berfore the function call: **Precondition**: **S and T are strings consisting of lowercase English letters. |S| = |T| and 2 <= |S| <= 100.**
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` takes two input strings `S` and `T` of equal length, consisting of lowercase English letters. It then checks if string `S` can be obtained by rotating string `T` and returns 'Yes' if it is possible, 'No' otherwise. The function may not handle edge cases where `S` cannot be formed by rotating `T` due to incomplete rotations or incorrect string lengths.

