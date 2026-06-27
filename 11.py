import pandas as pd
import sys

with open('out.txt','w') as f:
    # pandas\example\example_000.csv
    for _ in range(200):
        print(_)
        df=pd.read_csv(f".\pandas\input\input_{_:>03}.csv")
        # print(df)
        n=df['id'].size
        r=[[0]*n for _ in range(n)]
        df=df.sort_values(['A','id'],ascending=[False,True])
        df=df[0:int(0.9*n)]
        df=df.sort_values('id')
        n=int(0.9*n)
        id=df['id'].tolist()
        a=df['A'].tolist()
        b=df['B'].tolist()
        c=df['C'].tolist()
        d=df['D'].tolist()
        e=df['E'].tolist()
        for i in range(n):
            for j in range(n):
                r[i][j]=2*a[i]*a[j]+b[i]*b[j]-c[i]*c[j]+d[i]*d[j]-2*e[i]*e[j]
        cnt=set()
        t=[0]*n
        for i in range(n):
            for j in range(n):
                if i<=j:
                    continue
                for k in range(n):
                    if j<=k:
                        continue
                    tmp=r[i][j]*r[j][k]*r[k][i]
                    if tmp>=20000:
                        if (j,k,i) in cnt or (k,i,j) in cnt or (i,j,k) in cnt:
                            continue
                        cnt.add((i,j,k))
                        t[i]+=1
                        t[j]+=1
                        t[k]+=1
        f.write(f'Test Case: {_:>03}\n')
        f.write(f'{len(cnt)}\n')
        ans=list(enumerate(t))
        ans.sort(key=lambda x:(-x[1],x[0]))
        for i,x in enumerate(ans):
            if i>=5:
                break
            f.write(f'{id[x[0]]} {x[1]}\n')
