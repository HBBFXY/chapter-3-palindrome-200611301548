num = input("请输入一个5位数字：")
if len(num) != 5 or not num.isdigit():
    print("错误提示")
else:
 reversed_num = num[::-1] 
    if num == reversed_num:
        print("是回文数")
    else:
        print("不是回文数")
