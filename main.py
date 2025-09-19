def is_palindrome():
    # 从键盘输入一个5位数字
    num = input("请输入一个5位数字: ")
    
    # 验证输入是否为5位数字
    if not num.isdigit() or len(num) != 5:
        print("错误：请输入一个5位数字！")
        return
    
    # 判断是否为回文数
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

# 调用函数
is_palindrome()
