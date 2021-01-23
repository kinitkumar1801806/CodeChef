N=int(input())
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
j=0
word=""
m,n=16,0
for i in range(0,N):
    M=int(input())
    ls=list(input())
    for l in ls:
        if(l=='0'):
            p=abs(m-n)//2
            m=m-p
        else:
            n=(m+n)//2
        j+=1
        if j%4==0:
            ans=(m+n)//2
            word+=lst[ans]
            m,n=16,0
    print(word)
    word=""
