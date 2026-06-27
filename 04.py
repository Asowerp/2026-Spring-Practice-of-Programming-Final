import sys
from collections import defaultdict

input=sys.stdin.readline

q=int(input())

a={'':{},}

for _ in range(q):
    s=input().split()
    if s[0]=='ADD':
        course,project,ddl,tag=s[1],s[2],s[3],s[4]
        if course not in a:
            a[course]={}
        a[course][project]={'due':ddl,'tag':tag,'done':False}
    elif s[0]=='DONE':
        course,project=s[1],s[2]
        if course not in a or project not in a[course]:
            print("Not Found")
        else:
            a[course][project]['done']=True
    elif s[0]=='QUERY':
        course=s[1]
        if course not in a:
            print('Empty')
            continue
        ddl=[]
        for project in a[course]:
            if a[course][project]['done'] is False:
                ddl.append((a[course][project]['due'],project,a[course][project]['tag']))
        if len(ddl)==0:
            print('Empty')
            continue
        ddl.sort()
        for x in ddl:
            print(x[1],x[0],x[2])
    else:
        date=s[1]
        cnt=0
        for course in a:
            for project in a[course]:
                if a[course][project]['due']<=date and a[course][project]['done'] is False:
                    cnt+=1
                    # print(a[course][project]['due'],course,project)
        print(cnt)
        
# print(a)
