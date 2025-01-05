#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 100000, and v is a list of n integers where each integer v_i satisfies 1 <= v_i <= 100000.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100000; `m` contains the sums of `len(even) - evenc_most_common[i][1]` and `len(odd) - oddc_most_common[j][1]` for each valid comparison of `evenc_most_common` and `oddc_most_common` where the first elements are not equal; `m` may have 0, 1, 2, or more elements depending on the comparisons made.
    print(min(m))
#Overall this is what the function does:The function accepts an even integer `n` (between 2 and 100,000) and a list `v` of `n` integers (each between 1 and 100,000). It separates the integers in `v` into even and odd indexed elements, counts the occurrences of each integer in both groups, and then calculates the minimum number of elements that need to be removed from `v` such that the most common integer in the even indexed elements is different from the most common integer in the odd indexed elements. The function finally prints this minimum value.

