# a program squarecolor.py that reads a square identifier (e.g. e5) from the keyboard and prints the color (Black or White)
x=str(input('please enter squers alphapet'))  #ente the alphapet that define the colom alphapet
number=int(input('please enter a asquers nmuber'))#enter the number that define the row number
if number<=8 and number>=1:
    if (x==('a' or 'c' or 'e' or 'g'))and(number%2==0):
        print(x,number,'is white')
    elif (x==('a' or 'c' or 'e' or 'g')) and(number%2!=0):
        print(x,number,'is black')
    elif (x==('b' or 'd' or 'f' or 'h'))and(number%2==0):
        print(x,number,'is black')
    elif (x==('b' or 'd' or 'f' or 'h'))and(number%2!=0):
        print(x,number,'is white')
    else:
        print(' please inter a correct squers alphapet')
else:
    print('inter a correct squers number')

