def check(ls1,ls2,count,n,m):
    if sum(ls1)<=sum(ls2) and (count<=min(n,m)):
        m1=ls1.index(min(ls1))
        m2=ls2.index(max(ls2))
        ls1[m1],ls2[m2]=ls2[m2],ls1[m1]
        count+=1
        check(ls1,ls2,count,n,m)
    else:
        if(count>min(n,m)):
            print("-1")
        else:
            print(count)
k=int(input())        
for i in range(0,k):
    n,m=map(int,input().split())
    ls1=list(map(int,input().split(' ')))
    ls2=list(map(int,input().split(' ')))
    l1=sum(ls1)
    l2=sum(ls2)
    check(ls1,ls2,0,n,m)
