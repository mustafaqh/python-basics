# a program which reads a (positive) monthly income from the keyboard and then prints the corresponding income tax
i=int(input('Please provide monthly income')) 
if i < 0:
    print('you should provid positive income')
else:
    if i < 38000:
         t= i*0.3
         x=round(t)
         r=i-x
         print('Corresponding income tax:', x)
         print('your net income:', r)
    elif i>= 38000 and i<50000:
        i1=i-37999
        t1=37999*0.3
        t2=i1*0.35
        t=t1+t2
        x=round(t)
        r=i-x
        print('Corresponding income tax:', x)
        print('your net income', r)
    else:
        t1=37999*0.3
        t2=(49999-37999)*0.35
        i2=i-49999
        t3=i2*0.4
        t=t1+t2+t3
        x=round(t)
        r=i-x
        print('Corresponding income tax:', x)
        print('your net income', r)
