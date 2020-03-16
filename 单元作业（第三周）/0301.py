import math
a = int(input('Please enter the number(1~1000)：'))
if a >= 100 or a <= 1:
    print("请输入正确的数字")
i = j = 1
while i < 1000:
    i += 1
    if i % a == 0:
        print(j,i)
        j += 1