#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 2 × 10^5, and S is a string of length N consisting only of the characters `.` and `#`.
def func():
    n = int(raw_input())
    s = raw_input()
    temp = s.count('#')
    if (temp == 0 or temp == n) :
        print(0)
    else :
        head = 0
        tail = n - temp
        ret = tail + head
        for c in s:
            if c == '#':
                head += 1
            else:
                tail -= 1
            
            temp2 = head + tail
            
            if temp2 < ret:
                ret = temp2
            
        #State of the program after the  for loop has been executed: `N` is an integer such that \(1 \leq N \leq 2 \times 10^5\), `S` is a string of length `N` consisting only of the characters `.` and `#`, `n` is an input integer within the range \(1 \leq N \leq 2 \times 10^5\), `s` is a string of length `N` consisting only of the characters `.` and `#`, `temp` is the number of `#` characters in `s`, `head` is `temp`, `tail` is 0, `ret` is the minimum value of `head + tail` observed during the loop, which is the minimum of `temp` and any intermediate values of `head + tail`.
        print(ret)
    #State of the program after the if-else block has been executed: *`N` is an integer such that 1 ≤ N ≤ 2 × 10^5, `S` is a string of length `N` consisting only of the characters `.` and `#`, `n` is an input integer within the range 1 ≤ N ≤ 2 × 10^5, `s` is a string of length `N` consisting only of the characters `.` and `#`, `temp` is the number of `#` characters in `s`. If `temp` is 0 or `temp` is equal to `n`, the program does nothing. Otherwise, `head` is set to `temp`, `tail` is set to 0, and `ret` is the minimum value of `head + tail` observed during the loop, which is the minimum of `temp` and any intermediate values of `head + tail`. The value of `ret` has been printed.
#Overall this is what the function does:The function reads an integer `N` and a string `S` of length `N` from the standard input. The string `S` consists only of the characters `.` and `#`. The function calculates and prints the minimum number of moves required to make all `#` characters adjacent to each other in the string. A move is defined as changing one character in the string from `.` to `#` or from `#` to `.`. If the string `S` contains only `.` characters or only `#` characters, the function prints `0`. The function does not modify the original string `S` or the integer `N`. The final state of the program includes the printed result, which is the minimum number of moves required.

