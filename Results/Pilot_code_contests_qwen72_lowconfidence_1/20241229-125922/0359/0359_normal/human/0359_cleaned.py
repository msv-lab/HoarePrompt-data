class Parser(object):

    def __init__(self, string, pairs):
        self.string = string
        self.str_len = len(string)
        self.pairs = pairs

    def min_deletions(self):
        deletions = 0
        start = -1
        for pair in self.pairs:
            a = pair[0]
            b = pair[1]
            a_count = b_count = 0
            i = 0
            start = -1
            stop = -1
            while i < self.str_len:
                if a == self.string[i]:
                    a_count += 1
                    if start == -1:
                        start = i
                elif b == self.string[i]:
                    b_count += 1
                    if start == -1:
                        start = i
                elif start != -1:
                    stop = i
                    if stop != start:
                        if a_count > b_count:
                            subs = a * a_count
                            deletions += b_count
                            i = start + a_count
                            self.str_len -= b_count
                        else:
                            subs = b * b_count
                            deletions += a_count
                            i = start + b_count
                            self.str_len -= a_count
                        a_count = b_count = 0
                        self.string = self.string[:start] + subs + self.string[stop:]
                    start = -1
                i += 1
        if start != -1 and stop == -1:
            if a_count > b_count:
                deletions += b_count
            else:
                deletions += a_count
        return deletions

def func_1():
    string = raw_input()
    pairs_num = input()
    pairs = []
    i = 0
    while i < pairs_num:
        pair = raw_input()
        pairs.append(pair)
        i += 1
    parser = Parser(string, pairs)
    print(parser.min_deletions())
if __name__ == '__main__':
    func_1()