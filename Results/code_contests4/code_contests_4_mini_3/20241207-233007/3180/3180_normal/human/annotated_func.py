#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 100000, and v is a list of n integers where each integer is in the range 1 to 100000.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 <= `n` <= 100000; `m` contains values based on the evaluations of the condition for all combinations of `i` and `j`, where each appended value is the sum of `len(even) - evenc_most_common[i][1]` and `len(odd) - oddc_most_common[j][1]` for pairs where the elements at the first indices of `evenc_most_common` and `oddc_most_common` are not equal.
    print(min(m))
#Overall this is what the function does:The function accepts an even integer `n` (2 ≤ n ≤ 100000) and a list `v` of `n` integers (1 ≤ v[i] ≤ 100000). It separates the integers in `v` into even and odd indexed groups, counts the occurrences of each value in those groups, and calculates the minimum number of changes required to make the two groups distinct by finding the sum of elements that need to be changed. It returns this minimum value.

