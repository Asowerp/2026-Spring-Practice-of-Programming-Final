import bs4

rep=0
lzl=0
author=set()
cnt1=[0,0,0]
cnt2=[0,0,0]

for _ in range(1,201):
    soup=bs4.BeautifulSoup(open(f'./bs4v3_946/post_{_}.html',encoding='utf-8'),'html.parser')
    a=soup.find_all('a',class_='head-name')
    for x in a:
        author.add(x.text)
    for div in soup.find_all('div',class_='pb-content-item'):
        cnt1[0]+=div.text.count('出院')
        cnt2[0]+=div.text.count('怎么')
    for div in soup.find_all('div',class_='virtual-list-item'):
        # print(div)
        r=div.find_all('div',class_='comment-content')
        for x in r:
            for comment in x.find_all('div',class_='pb-content-item'):
                cnt1[1]+=comment.text.count('出院')
                cnt2[1]+=comment.text.count('怎么')
        rep+=len(r)
        l=div.find_all('div',class_='pb-lzl-item')
        for x in l:
            for comment in x.find_all('div',class_='pb-content-item'):
                cnt1[2]+=comment.text.count('出院')
                cnt2[2]+=comment.text.count('怎么')
        lzl+=len(l)

cnt1[0]-=cnt1[1]+cnt1[2]
cnt2[0]-=cnt2[1]+cnt2[2]

print(rep)
print(lzl)
print(len(author))
print(*cnt1)
print(*cnt2)
