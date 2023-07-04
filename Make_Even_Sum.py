n=int(input())
m=input()
arr=list(map(int,m.split()))
s=sum(arr)
if s%2==0:
    print(1)
else:
    print(0)