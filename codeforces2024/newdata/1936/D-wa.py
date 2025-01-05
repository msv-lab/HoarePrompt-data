class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
    
    def build(self, data):
        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, pos, value):
        # Update the value at position pos
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])
    
    def query(self, left, right):
        # Query the maximum value in the range [left, right)
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                result = max(result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = max(result, self.tree[right])
            left //= 2
            right //= 2
        return result

import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, v = int(data[index]), int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + n]))
        index += n
        q = int(data[index])
        index += 1
        
        seg_tree = SegmentTree(a)
        
        for __ in range(q):
            query_type = int(data[index])
            if query_type == 1:
                i, x = int(data[index + 1]) - 1, int(data[index + 2])
                index += 3
                b[i] = x
            elif query_type == 2:
                l, r = int(data[index + 1]) - 1, int(data[index + 2]) - 1
                index += 3
                
                min_beauty = float('inf')
                current_or = 0
                j = l
                
                for i in range(l, r + 1):
                    while j <= r and current_or < v:
                        current_or |= b[j]
                        j += 1
                    if current_or >= v:
                        min_beauty = min(min_beauty, seg_tree.query(i, j))
                    current_or &= ~b[i]
                
                if min_beauty == float('inf'):
                    results.append("-1")
                else:
                    results.append(str(min_beauty))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()