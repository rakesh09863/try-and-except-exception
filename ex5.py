try:
    s1=input('enter the first value:')
    s2=input('enter the second value:')
    a=int(s1)
    b=int(s2)
    c=a/b
    s='python'
    print(s[10])
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
except:#default except block
    print('oopps some thing is wrong')
else:
    print('first value={}'.format(a))
    print('second value={}'.format(b))
    print('div={}'.format(c))
finally:
    print('-----finally block-----')
    print('program is completed')