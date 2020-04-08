from decimal import*
getcontext().prec=150
decpi=Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762')
getcontext().rounding=ROUND_HALF_UP
def decsin(t):
    t=t%(2*decpi)
    v,c,s,u,i,o=Decimal(1),Decimal(0),Decimal(t),Decimal(1),Decimal(t),Decimal(1)
    while s!=c:
        c=s
        v+=2
        u*=v*(v-1)
        i*=t*t
        o*=-1
        s+=i/u*o
    return Decimal(s)
a,s,d=map(Decimal,input().split())
t=Decimal()
e=Decimal(0)
r=Decimal(500000)
w=Decimal(1.0e-60)
while(Decimal(r-e).copy_abs())>=w:
    t=(e+r)/2
    if Decimal(a*t+s*decsin(t))<Decimal(d):
        e=t
    else:
        r=t
print(round(t,6))
