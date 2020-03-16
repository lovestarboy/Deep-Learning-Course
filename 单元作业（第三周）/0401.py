i = 0
while i <= 3:
    if (i == 3):
        print("对不起，您已经3次输入错误，程序退出。")
        break
    num = input('请输入一个整数：')
    # print(num)
    number = int(num)
    is_int = num.isdigit()
    # print(is_int)
    if  is_int == False:
        print("对不起，您输入的不是整数！")
    elif number <= 1 or number >= 100:
        print("对不起，您输入的数字范围不正确")
    else:
        print("您输入的整数是: %s"%(num))
        break
    i += 1