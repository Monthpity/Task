#已知三角形的边长求三角形的面积和周长
import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    d=a+b+c
    e=(a+b+c)/2
    f=math.sqrt(e*(e-a)*(e-b)*(e-c))
    print('三角形的周长为：'+str(d))
    print('三角形的面积为：%.2f' % f)
else:
     print('三条变得长度不能构成三角形')