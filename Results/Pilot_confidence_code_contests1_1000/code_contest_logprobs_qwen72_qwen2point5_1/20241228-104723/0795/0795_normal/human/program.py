import sys

lines = sys.stdin.readlines()
N = int(lines[0])
h_vec = [int(i) for i in lines[1].split(' ')]
#N = len(h_vec)
h_vec.append(0) # Fixes an edge case.

R = 1000000007

summ = 0
prev = 0

for i in xrange(N-1, 0, -1):
    result = min(h_vec[i] - 1, h_vec[i-1] - 1) + min(h_vec[i] - 1, h_vec[i-1] - 1, h_vec[i+1] - 1) * prev

    prev = result
    prev %= R

    left_boundary = min(h_vec[i-1] - 1, h_vec[i] - 1)

    summ += left_boundary * result
    summ %= R

single_sum = sum(h_vec) - N

summ += single_sum
summ %= R

sys.stdout.write(str(summ))