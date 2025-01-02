#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 100,000, and a list of n non-negative integers ai is provided, where at least n - 1 of these integers are beautiful numbers (a beautiful number is defined as a number consisting only of the digits '1' and '0', with at most one digit '1'). The total length of all these numbers' representations does not exceed 100,000.
def func():
    n = int(raw_input())
    a = raw_input().split()
    if ('0' in a) :
        sys.stdout.write('0')
        exit()
    #State of the program after the if block has been executed: *`n` is an integer where 1 ≤ n ≤ 100,000, `a` is a list of n strings representing non-negative integers, where at least n - 1 of these integers are beautiful numbers, and the total length of all these numbers' representations does not exceed 100,000. If the list `a` contains at least one '0', a '0' has been written to the standard output and the program has exited.
    zc = 0
    hasBad = False
    for x in a:
        f = True
        
        c = 0
        
        c1 = 0
        
        for ch in x:
            if ch == '0':
                c += 1
            if ch == '1':
                c1 += 1
            if ch != '1' and ch != '0' or c1 > 1:
                f = False
                break
        
        if f:
            zc += c
        else:
            hasBad = True
            sys.stdout.write(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ n ≤ 100,000, `a` is a list of n strings representing non-negative integers (with no '0' and at least n - 1 beautiful numbers), the total length of all these numbers' representations does not exceed 100,000. `zc` is the total count of '0' characters in all the strings in `a` that consist only of '0' and '1' characters and contain exactly one '1'. `hasBad` is True if any string in `a` does not meet the criteria of being a beautiful number (i.e., contains characters other than '0' or '1', or contains more than one '1'), otherwise `hasBad` is False. If `hasBad` is True, the first string in `a` that does not meet the criteria has been written to the standard output.
    if (not hasBad) :
        sys.stdout.write('1')
    #State of the program after the if block has been executed: *`n` is an integer where 1 ≤ n ≤ 100,000, `a` is a list of n strings representing non-negative integers (with no '0' and at least n - 1 beautiful numbers), the total length of all these numbers' representations does not exceed 100,000. `zc` is the total count of '0' characters in all the strings in `a` that consist only of '0' and '1' characters and contain exactly one '1'. If `hasBad` is False, indicating that all strings in `a` meet the criteria of being beautiful numbers, a '1' has been written to the standard output. If `hasBad` is True, the first string in `a` that does not meet the criteria has been written to the standard output.
    sys.stdout.write('0' * zc)
#Overall this is what the function does:The function processes a list of strings representing non-negative integers, where each integer is expected to be a beautiful number (consisting only of the digits '1' and '0', with at most one digit '1'). The function performs the following actions:

1. Reads an integer `n` and a list of `n` strings from the standard input.
2. If the list contains the string '0', the function writes '0' to the standard output and exits immediately.
3. If the list does not contain '0', the function iterates through the list to check if each string is a beautiful number. If any string is not a beautiful number, the function writes that string to the standard output and exits.
4. If all strings in the list are beautiful numbers, the function counts the total number of '0' characters in all the strings that consist only of '0' and '1' and contain exactly one '1'.
5. The function then writes '1' followed by the counted number of '0' characters to the standard output.

Final State:
- The function either writes '0' and exits if '0' is found in the list.
- Or, if a non-beautiful number is found, it writes that number and exits.
- Otherwise, it writes '1' followed by the total count of '0' characters in all beautiful numbers and exits.

Edge Cases:
- If the list contains '0', the function writes '0' and exits without further processing.
- If the list contains a non-beautiful number, the function writes that number and exits.
- If all numbers are beautiful, the function writes '1' followed by the count of '0' characters in those numbers.

