#State of the program right berfore the function call: ** n and m are integers such that 3 ≤ n ≤ 200,000 and 1 ≤ m ≤ 200,000. u_i and v_i are integers such that 1 ≤ u_i, v_i ≤ n and u_i ≠ v_i.
def func_1():
    return int(raw_input())
    #The program returns the integer input value after converting it to an integer
#Overall this is what the function does:The function `func_1` reads an input value and returns it as an integer. The function does not have any error handling or validation for non-integer inputs. It simply converts the input to an integer and returns it.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= 200,000 and 1 <= m <= 200,000. u_i and v_i are integers such that 1 <= u_i, v_i <= n and u_i ≠ v_i.**
def func_2():
    return list(map(int, raw_input().split()))
    #The program returns a list of integers obtained by mapping the input values provided by the user
#Overall this is what the function does:The function `func_2` takes user input, splits it into individual values, converts them to integers, and returns them as a list. The function does not specify any constraints on the input values or handle any exceptions that may occur during the conversion process.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 200,000.**
def func_3(n):
    stdout.write(str(n) + '\n')
#Overall this is what the function does:The function `func_3` accepts an integer parameter `n` within the range 3 to 200,000 and prints the value of `n` followed by a new line. The function does not have a specific return value specified.

#State of the program right berfore the function call: n and m are integers such that 3 <= n <= 200,000 and 1 <= m <= 200,000. arr is a list of tuples where each tuple contains two integers u_i and v_i such that 1 <= u_i, v_i <= n and u_i ≠ v_i.**
def func_4(arr):
    pr(' '.join(map(str, arr)) + '\n')
#Overall this is what the function does:The function `func_4` accepts a parameter `arr`, which is a list of tuples. Each tuple in the list contains two integers `u_i` and `v_i` such that 1 <= `u_i`, `v_i` <= n and `u_i` ≠ `v_i`. The function then prints the elements of the tuples separated by a space. No specific output is returned from the function.

#State of the program right berfore the function call: **
def func_5():
    return map(int, stdin.read().split())
    #The program returns a map object containing the integers parsed from the input read from stdin
#Overall this is what the function does:The function `func_5` does not accept any parameters. It returns a map object containing the integers parsed from the input read from stdin.

