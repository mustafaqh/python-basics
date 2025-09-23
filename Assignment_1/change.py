#a program that computes the change a customer should receive for paid for a certain sum
p = float(input('inter price')) #Price
m =float(input('inter payment')) #Payment
x=round(p) #round off p
c=m-x # the rest
t=c//1000 # integer devision howmany 1000 fit in c
fh=c//500 # howmany 500 fit in c
r=c%500   #modulus
tvh=r//200 
e=r//100
r1=r%100
f=r1//50
r2=r1%50
tj=r2//20
r3=r2%20
ti=r3//10
r4=r3%10
fe=r4//5
r5=r4%5
tv=r5//2
r6=r5%2
en=r6//1
print('price',p)
print('payment',m)
print('change',c,'kr')
print('1000 bills :',t)
print('500 bills:',fh)
print('200 bills:',tvh)
print('100 bills:',e)
print('50 bills:',f)
print('20 bills:',tj)
print('10 coins:',ti)
print('5 coins:',fe)
print('2 coins:',tv)
print('1 coins:',en)
