import sys
from collections import defaultdict

input=sys.stdin.readline

n=int(input())
dish=[input().strip() for _ in range(n)]
first={}
cnt=defaultdict(int)

for i,x in enumerate(dish):
    if x not in first:
        first[x]=i
    cnt[x]+=1

dish=list(set(dish))
dish.sort(key=lambda x:first[x])

for x in dish:
    print(x,cnt[x])
