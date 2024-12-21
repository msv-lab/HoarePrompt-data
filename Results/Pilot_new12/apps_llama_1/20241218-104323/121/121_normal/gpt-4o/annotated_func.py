#State of the program right berfore the function call: The input consists of an integer n (4 ≤ n ≤ 255) and a string s of length n, where s consists of the characters 'A', 'C', 'G', 'T', and '?' and n is divisible by 4.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns None
    #State of the program after the if block has been executed: `n` is an integer equal to `int(data[0])`, `s` is a string equal to `data[1]`, `data` is a list of strings split from the content of the `input` variable, and `n` is divisible by 4 with no remainder, i.e., `n % 4 == 0`.
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer equal to `int(data[0])` and is divisible by 4 with no remainder, `s` is a string equal to `data[1]`, `data` is a list of strings split from the content of the `input` variable, `target_count` is `n // 4`, `counts` is a dictionary with keys `'A'`, `'C'`, `'G'`, `'T'` where the values represent the frequency of each character in the string `s`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is an integer equal to `int(data[0])` and is divisible by 4 with no remainder, `s` is a string equal to `data[1]`, `data` is a list of strings split from the content of the `input` variable and has at least 2 elements, `target_count` is `n // 4`, `counts` is a dictionary with keys `'A'`, `'C'`, `'G'`, `'T'` where the values represent the frequency of each character in the string `s`, and either all values in `counts` are less than or equal to `target_count` if the loop completes, or the function has printed `'==='` and returned if any value in `counts` exceeds `target_count`.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer and a multiple of 4, `s` is a string equal to `data[1]`, `data` is a list of strings with at least 2 elements, `target_count` is `n // 4`, `counts` is a dictionary with keys `'A'`, `'C'`, `'G'`, `'T'` where each value represents the final count of characters after the loop executions and is less than or equal to `target_count`, and `result` is a list of characters updated based on the loop conditions.
    print(''.join(result))
#Overall this is what the function does:The function reads input from the standard input, expecting an integer `n` (where 4 ≤ `n` ≤ 255) and a string `s` of length `n`, consisting of characters 'A', 'C', 'G', 'T', and '?', with `n` being divisible by 4. It counts the frequency of each character 'A', 'C', 'G', 'T' in the string `s` and checks if any of these counts exceed `n / 4`. If `n` is not divisible by 4 or if any character count exceeds `n / 4`, it prints '===' and does not return an explicit value. If the counts are within the limit, it replaces '?' characters in the string with 'A', 'C', 'G', 'T' to ensure each of these characters appears exactly `n / 4` times, and then prints the modified string. The function does not handle cases where the input may not match the expected format or where the '?' characters cannot be replaced to meet the `n / 4` requirement for all characters due to insufficient '?' characters in the string. In all cases, the function does not return an explicit value.

