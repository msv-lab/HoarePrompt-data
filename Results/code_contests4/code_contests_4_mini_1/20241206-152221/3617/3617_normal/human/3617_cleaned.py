def func_1(argv):
    line = sys.stdin.readline().rstrip('\n')
    while line:
        N = int(line)
        A = [int(a) for a in raw_input().rstrip('\n').split(' ')]
        diff = sorted([a - (i + 1) for (i, a) in enumerate(A)])
        m = []
        for i in range(N):
            left = 0
            for j in range(0, i):
                left += abs(diff[j] - diff[i])
            right = 0
            for j in range(i + 1, N):
                right += abs(diff[j] - diff[i])
            m.append(left + right)
        print(min(m))
        line = sys.stdin.readline().rstrip('\n')
if __name__ == '__main__':
    func_1(sys.argv)