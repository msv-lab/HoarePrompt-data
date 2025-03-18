#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n is an integer such that 1 <= n <= 100 for each test case, and a_1, a_2, ..., a_n are integers such that 1 <= a_i <= 100.
def func():
    w = int(input())
    for _ in range(w):
        ln = int(input())
        
        palka = list(map(int, input().split()))
        
        pl = []
        
        d = {}
        
        for i in palka:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
            if i not in pl:
                pl.append(i)
        
        shapes = 0
        
        for j in pl:
            if d[j] >= 3:
                shapes += d[j] // 3
        
        print(shapes)
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is an integer such that 1 <= n <= 100 for each test case, `a_1, a_2, ..., a_n` are integers such that 1 <= a_i <= 100, `w` is 0, `_` is `w-1`, `ln` is an input integer, `palka` is a list of integers input by the user, `pl` is a list containing all unique integers from `palka` in the order they first appeared, `d` is a dictionary where each key is an integer from `palka` and each value is the count of how many times that integer appears in `palka`, `shapes` is the sum of `d[j] // 3` for all elements `j` in `pl` that appear at least 3 times in `palka` for each iteration of the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers, all within the range [1, 100]. It then calculates the number of groups of three identical integers that can be formed from the list and prints this number for each test case. After processing all test cases, the function does not return any value, but the state of the program includes `w` being 0, `_` being `w-1` (which is -1), `ln` being the last input integer, `palka` being the last list of integers input by the user, `pl` being a list of all unique integers from `palka` in the order they first appeared, `d` being a dictionary with counts of each integer in `palka`, and `shapes` being the sum of `d[j] // 3` for all elements `j` in `pl` that appear at least 3 times in `palka`.

