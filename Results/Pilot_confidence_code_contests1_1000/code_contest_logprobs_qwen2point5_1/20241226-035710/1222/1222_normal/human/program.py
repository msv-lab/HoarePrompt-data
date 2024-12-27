input = raw_input

k = int(input())

suf_dict = {}
for d in range(10):
    if d == 0:
        suf_dict[str(d)] = ["0", "1"]
    elif d == 1:
        suf_dict[str(d)] = ["0", "1", "2"]
    elif d == 9:
        suf_dict[str(d)] = ["8", "9"]
    else:
        suf_dict[str(d)] = [str(d-1), str(d), str(d+1)]


def find(x):
    sufs = suf_dict[x[-1]]
    ret = [x+suf for suf in sufs]
    return ret

def main():
    xs = list("123456789")
    last_count = 9
    if k <= 9:
        out = k
        return out
    else:
        while True:
            next_xs = []
            for x in xs:
                first_count = last_count + 1
                elms = find(x)
                cur_num = len(elms)
                last_count = first_count + cur_num - 1
                #print(first_count, last_count, elms)
                if first_count <= k <= last_count:
                    out = elms[k-first_count]
                    return out
                next_xs += elms
            xs = next_xs

out = main()
print(out)