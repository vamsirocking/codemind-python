for _ in range(int(input())):
    a,n=map(int,input().split())
    l=input()
    m=l
    if n%2==0:
        for l in range (n,0,-1):
            if l%2==0:
                m=m[1:l]+m[0]+m[l:]
    elif n%2==1:
            for s in range(n,0,-1):
                if s%2==1:
                    r=s
                    m=m[1:r]+m[0]+m[r:]
    print(m)