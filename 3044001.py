import math
a = float(input('Please enter the number a：'))
b = float(input('Please enter the number b：'))
c = float(input('Please enter the number c：'))
if a == 0:
    print("a不能为0哦！")
else:
    num = b ** 2 - 4 * a *c
    if num < 0:
        print("此方程无解！")
    elif num == 0:
        print("此方程有一个实数根是：",end=" ")
        x = float(-b/(2*a))
        print("x = %.2f"%x)
    else:
        print("此方程有两个实数根分别是：",end=" ")
        x1 = float((-b+math.sqrt(num))/(2*a))
        x2 = float((-b-math.sqrt(num))/(2*a))
        print("x1 = %.2f,x2 = %.2f"%(x1,x2))
