class FenwickTree:

    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | i + 1
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return (idx + 1, k)

class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = bisect_left(self.macro, x)
        j = bisect_right(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = (self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:])
            self.micro_size[i:i + 1] = (self.block_size >> 1, self.block_size >> 1)
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        (i, j) = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        (i, j) = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.bisect_right(x) - self.bisect_left(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def bisect_left(self, x):
        i = bisect_left(self.macro, x)
        return self.fenwick(i) + bisect_left(self.micros[i], x)

    def bisect_right(self, x):
        i = bisect_right(self.macro, x)
        return self.fenwick(i) + bisect_right(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))

def func_1(func):
    d = {}

    def wrapper(*args):
        if args not in d:
            d[args] = func(*args)
        return d[args]
    return wrapper

def func_2():
    return sys.stdin.readline().strip()

def func_3():
    return int(func_2())

def func_4(delimiter=' '):
    return list(map(int, func_2().split(delimiter)))

def func_5():
    return func_2()

def func_6():
    (n, m, k) = func_4()
    A = func_4()
    D = sorted(set(func_4()))
    F = func_4()
    (max_diff, next_max_diff, index) = (-inf, -inf, None)
    for i in range(1, n):
        diff = A[i] - A[i - 1]
        if diff > max_diff:
            next_max_diff = max_diff
            max_diff = diff
            index = i
        elif diff > next_max_diff:
            next_max_diff = diff
    (left, right) = (A[index - 1], A[index])
    ans = max_diff
    for f in F:
        l = bisect_right(D, left - f)
        h = bisect_left(D, right - f) - 1
        while l < h:
            mid = l + (h - l) // 2
            (mid_sum, mid_next_sum) = (D[mid] + f, D[mid + 1] + f)
            if mid_sum - left < right - mid_next_sum:
                l = mid + 1
            else:
                h = mid
        if l == h:
            ans = min(ans, max(D[l] + f - left, right - D[l] - f))
    print(max(ans, next_max_diff))

def func_7():
    testcases = func_3()
    for _ in range(testcases):
        func_6()
if __name__ == '__main__':
    if path.exists('input.txt'):
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    func_7()