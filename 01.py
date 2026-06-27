import sys

input=sys.stdin.readline

a=list(map(int,input().split()))

t={1:11,11:10,12:10,13:10}
ans=0
double=False

for x in a:
    if x in t:
        ans+=t[x]
    else:
        ans+=x
    if a.count(x)>1:
        double=True

print(ans*(double+1))
