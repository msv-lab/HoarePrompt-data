BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'A' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            (self.buffer.truncate(0), self.buffer.seek(0))

class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda : self.buffer.read().decode('ascii')
        self.readline = lambda : self.buffer.readline().decode('ascii')

def func_1(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    (sep, file) = (kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout))
    at_start = True
    for A in args:
        if not at_start:
            file.write(sep)
        file.write(str(A))
        at_start = False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False):
        file.flush()
if sys.version_info[0] < 3:
    (sys.stdin, sys.stdout) = (FastIO(sys.stdin), FastIO(sys.stdout))
else:
    (sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))

def func_2(f, stack=[]):

    def wrapped_func(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
                continue
            stack.pop()
            if not stack:
                break
            to = stack[-1].send(to)
        return to
    return wrapped_func

class SortedList:

    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[start:start + _load] for start in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for start in range(len(_fen_tree)):
            if start | start + 1 < len(_fen_tree):
                _fen_tree[start | start + 1] += _fen_tree[start]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()
        _fen_tree = self._fen_tree
        A = 0
        while end:
            A += _fen_tree[end - 1]
            end &= end - 1
        return A

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return (0, k)
        if k >= self._len - _list_lens[-1]:
            return (len(_list_lens) - 1, k + _list_lens[-1] - self._len)
        if self._rebuild:
            self._fen_build()
        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return (idx + 1, k)

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1
        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return (0, 0)
        _lists = self._lists
        _mins = self._mins
        (lo, pos) = (-1, len(_lists) - 1)
        while lo + 1 < pos:
            mi = lo + pos >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi
        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1
        _list = _lists[pos]
        (lo, idx) = (-1, len(_list))
        while lo + 1 < idx:
            mi = lo + idx >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi
        return (pos, idx)

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return (0, 0)
        _lists = self._lists
        _mins = self._mins
        (pos, hi) = (0, len(_lists))
        while pos + 1 < hi:
            mi = pos + hi >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi
        _list = _lists[pos]
        (lo, idx) = (-1, len(_list))
        while lo + 1 < idx:
            mi = lo + idx >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi
        return (pos, idx)

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
        self._len += 1
        if _lists:
            (pos, idx) = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            (pos, idx) = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        (pos, idx) = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        (pos, idx) = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        (pos, idx) = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        (pos, idx) = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        (pos, idx) = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            (pos, idx) = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))
mod = 1000000007
test_count = 1

def func_3(t):
    global test_count
    for p in range(t):
        func_30()
        test_count += 1

def func_4(A, B, p):
    res = 1
    A = A % p
    if A == 0:
        return 0
    while B > 0:
        if B & 1 == 1:
            res = res * A % p
        B = B >> 1
        A = A * A % p
    return res

def func_5(n):
    return set(reduce(list.__add__, ([start, n // start] for start in range(1, int(n ** 0.5) + 1) if n % start == 0)))

def func_6(a, b):
    if a == b:
        return a
    while b > 0:
        (a, b) = (b, a % b)
    return a

def func_7(ar):
    return list(accumulate(ar))

def func_8(ar):
    return list(accumulate(ar[::-1]))[::-1]

def func_9():
    return int(func_17())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def func_10():
    func_1('YES')

def func_11():
    func_1('NO')

def func_12():
    func_1('Yes')

def func_13():
    func_1('No')

def func_14(start):
    start = start - (start >> 1 & 1431655765)
    start = (start & 858993459) + (start >> 2 & 858993459)
    return ((start + (start >> 4) & 252645135) * 16843009 & 4294967295) >> 24

class MergeFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        to_update = []
        while a != self.parent[a]:
            to_update.append(a)
            a = self.parent[a]
        for b in to_update:
            self.parent[b] = a
        return self.parent[a]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            (a, b) = (b, a)
        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

def func_15(a, b):
    return abs(a // func_6(a, b) * b)

def func_16(n, r):
    if n < r:
        return 0
    else:
        return fac[n] * (finv[r] * finv[n - r] % mod) % mod

def func_17():
    return sys.stdin.readline().rstrip('\r\n')

def func_18(var):
    sys.stdout.write(str(var))

def func_19():
    return list(map(int, func_17().split()))

def func_20():
    return list(map(str, func_17().split()))

def func_21():
    return map(int, func_17().split())

def func_22():
    return map(str, func_17().split())

def func_23():
    return map(float, func_17().split())

def func_24():
    func_18('\n')

def func_25(n, v):
    return [v] * n

def func_26(n, m, v):
    return [[v] * m for _ in range(n)]

def func_27(n, m, p, v):
    return [[[v] * p for _ in range(m)] for start in range(n)]

def func_28(a, b):
    return (a + b - 1) // b

def func_29(s):
    func_1('Case #{}: {}'.format(test_count, s))

def func_30():
    (n, m, x) = func_21()
    x -= 1
    ans = x % n * m + x // n
    func_1(ans + 1)
func_3(func_9())