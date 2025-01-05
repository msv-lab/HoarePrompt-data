#State of the program right berfore the function call: n is an even integer greater than or equal to 2, and v_1, v_2, ..., v_n are integers ranging from 1 to 10^5.**
def func():
    n = int(raw_input())
    v = map(int, raw_input().split())
    even = [vi for i, vi in enumerate(v) if i % 2 == 0]
    odd = [vi for i, vi in enumerate(v) if i % 2 == 1]
    evenc = collections.Counter(even)
    oddc = collections.Counter(odd)
    evenc_most_common = evenc.most_common(len(set(even))) + [(None, 0)]
    oddc_most_common = oddc.most_common(len(set(odd))) + [(None, 0)]
    m = []
    for i in range(2):
        for j in range(2):
            if evenc_most_common[i][0] != oddc_most_common[j][0]:
                a = len(even) - evenc_most_common[i][1]
                b = len(odd) - oddc_most_common[j][1]
                m.append(a + b)
        
    #State of the program after the  for loop has been executed: `m` will contain the sum of differences between the lengths of `even` and the frequency of the most common element at index 2, and the lengths of `odd` and the frequency of the most common element at index 1, 2, and 2 for the three iterations. All other variables will remain the same as in the initial state.
    print(min(m))
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `v` from the user input. It then separates the even and odd elements from the list, counts the frequencies of each, and identifies the most common elements. After this, it calculates the sum of the differences between the lengths of the even and odd lists and the frequencies of the most common elements. Finally, it prints the minimum sum calculated. The function does not accept any parameters and operates solely on the user-provided inputs.

