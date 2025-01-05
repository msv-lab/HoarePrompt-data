n = int(raw_input())
v = map(int, raw_input().split())
even = [vi for (i, vi) in enumerate(v) if i % 2 == 0]
odd = [vi for (i, vi) in enumerate(v) if i % 2 == 1]
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
print(min(m))