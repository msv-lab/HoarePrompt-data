#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 100000, and v is a list of integers where each v_i satisfies 1 <= v_i <= 100000.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 <= `n` <= 100000; `m` contains the sums `a + b` for each valid comparison between the most common elements of `evenc` and `oddc`, where `a` is the number of even elements minus the frequency of the most common even element, and `b` is the number of odd elements minus the frequency of the most common odd element.
    print(min(m))
#Overall this is what the function does:The function accepts an even integer `n` (where 2 <= n <= 100000) and a list of integers `v` (where each element satisfies 1 <= v_i <= 100000). It calculates the minimum number of elements that need to be removed from `v` to ensure that the most common even and odd integers in the list are different. The function returns this minimum number.

