def btd(n):
    if (n>1):
        btd(n//2)
    print(n%2)
btd(8)

def dtb(b):
    d=0
    i=0
    while(b!=0):
        dec=b%10
        d=d+dec*pow(2,i)
        b=b//10
        i+=1
        print(b,dec,d,i)
    #print(d)
dtb(1000)
b=1000
b=b//10
