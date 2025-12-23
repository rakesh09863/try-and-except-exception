try:
    s1=input('enter the first value:')
    s2=input('enter the second value:')
    a=int(s1)
    b=int(s2)
    c=a/b
    print('first value={}'.format(a))
    print('second value={}'.format(b))
    print('div=',c)
    print('Program execution ended')
except ZeroDivisionError:
    print('do not enter Zero for den--')
except ValueError:
    print('do not enter alnumbs,stmbols and str')