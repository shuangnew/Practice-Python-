
def gen():
    n=input('How long is your Fionnaci number?')
    n=int(n)
    i=1
    if n==0:
        a=[]
    elif n==1:
        a=[1]
    elif n==2:
        a=[1,1]
    elif n>2:
        a=[1,1]
        while len(a)<=n-1:
            a.append(a[i]+a[i-1])
            i=i+1

    return a

print(gen())