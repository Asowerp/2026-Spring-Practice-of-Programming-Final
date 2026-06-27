def make_counter(start, step):
    cnt=0
    def counter():
        nonlocal cnt
        ret=start+cnt*step
        cnt+=1
        return ret
    return counter
counters = []
T = int(input())
for _ in range(T):
    parts = input().split()
    if parts[0] == "NEW":
        s, d = int(parts[1]), int(parts[2])
        counters.append(make_counter(s, d))
    else:
        idx = int(parts[1])
        print(counters[idx]())
