
class RangeMinimumQuery:
    nmemb = 1
    size  = 1
    data  = []
    def __init__(self, n):
        self.nmemb = n
        while self.size < n: self.size *= 2
        self.data = [0] * (self.size * 2)
        
    def __find(self, start, end, id, left, right):
        if end <= left or right <= start:
            return 2 ** 31 - 1
        elif start <= left and right <= end:
            return self.data[id]
        else:
            mid = (left + right) / 2
            vl = self.__find(start, end, id * 2 + 1, left, mid)
            vr = self.__find(start, end, id * 2 + 2, mid, right)
            return min(vl, vr)
            
    def find(self, start, end):
        return self.__find(start, end, 0, 0, self.size)
        
    def update(self, pos, value):
        pos += self.size - 1
        self.data[pos] = value
        
        while(pos > 0):
            pos = (pos - 1) / 2
            vl = self.data[pos * 2 + 1]
            vr = self.data[pos * 2 + 2]
            self.data[pos] = min(vl, vr)
            
if __name__ == "__main__":
    n, q = map(int, raw_input().split())
    rmq = RangeMinimumQuery(n)

    for i in range(n):
        rmq.update(i, 2 ** 31 - 1)
        assert(rmq.find(i, i + 1) == 2 ** 31 - 1)
        
    for i in range(q):
        com, x, y = map(int, raw_input().split())
        if com == 0:
            rmq.update(x, y)
        else:
            print(rmq.find(x, y + 1))
    
            
            
        
            