import sys
from collections import defaultdict

input=sys.stdin.readline

while True:
    try:
        s=input().strip()
    except EOFError:
        break
    if s=='':
        break
    a=s.split()
    l=[]
    for x in a:
        l.append(x.split('-'))
    l.sort(key=lambda x:(0 if x[0]=='X' else 1 if x[0]=='Y' else 2 if x[0]=='Z' else 3,x[1],-int(x[2])))
    for x in l:
        print(f'{x[0]}-{x[1]}-{x[2]}',end=' ')
    print()
