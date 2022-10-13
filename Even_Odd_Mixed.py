m=int(input())
ec=oc=0
while m>0:
    r=m%10
    if r%2==0:
        ec+=1
    else:
        oc+=1
    m=m//10
if ec==0:
    print("Odd")
elif oc==0:
    print('Even')
else:
    print("Mixed")
        