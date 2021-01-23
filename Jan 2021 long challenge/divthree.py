n=int(input())
for i in range(0,n):
    n,k,d=map(int,input().split(' '))
    ls=list(map(int,input().split(' ')))
    sum1=sum(ls)
    if sum1<k:
        ans=0
    elif sum1>=k:
        rem=sum1//k
        if rem>d:
            ans=d
        else:
            ans=rem
    print(ans)
