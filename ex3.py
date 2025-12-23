try:
    s1=input('enter the first value:')
    s2=input('enter the second value:')
    a=int(s1)
    b=int(s2)
    c=a/b
except(ZeroDivisionError,ValueError):
    print('don`t enter zeros')
    print('don`t enter string,special symbols')
else:
    print('first value={}'.format(a))
    print('second value={}'.format(b))
    print('div={}'.format(c))
finally:
    print('program is completed')

