n=int(input())
s=n**2
R=0
while n>0:
    r=n%10
    R=R*10+r
    n=n//10
sR=R**2
RR=0
while sR>0:
    r=sR%10
    RR=RR*10+r
    sR=sR//10
if RR==s:
    print(True)
else:
    print(False)
