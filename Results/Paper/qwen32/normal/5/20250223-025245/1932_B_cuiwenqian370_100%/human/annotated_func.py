#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 100) representing the number of signs. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the periodicities of the signs.
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n = int(data[index])
        
        index += 1
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        last_year = a[0]
        
        for i in range(1, n):
            next_year = (last_year + 1 + a[i] - 1) // a[i] * a[i]
            last_year = next_year
        
        results.append(str(last_year))
        
    #State: data is a list of strings containing all the input values split by whitespace; input holds the entire input string; index points to the position right after the last element of the last test case; T is 0; results is a list containing the string representation of last_year for each test case.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a number of signs and their respective periodicities. It calculates the synchronized blinking periodicity for all signs in each test case and outputs the result for each test case.

