import sys
from collections import defaultdict

input=sys.stdin.readline

n,m,t=map(int,input().split())

mp=[]

for _ in range(n):
    s=input().strip()
    mp.append([int(ch) for ch in s])

for _ in range(t):
    nxt=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cnt=0
            for dir in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                x=i+dir[0]
                y=j+dir[1]
                if not (0<=x<n and 0<=y<m):
                    continue
                cnt+=mp[x][y]
            nxt[i][j]=(1 if (mp[i][j]==1 and 2<=cnt<=3) or (mp[i][j]==0 and cnt==3) else 0)
    mp,nxt=nxt,mp

for x in mp:
    print(*x,sep='')
