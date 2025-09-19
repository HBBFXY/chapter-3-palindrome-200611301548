def is_palindrome_five_digit():
    # 获取用户输入
    num_input = input("请输入一个5位数字：")
    
    # 验证输入长度和是否为纯数字
    if len(num_input) != 5 or not num_input.isdigit():
        print("错误提示")
        return
    
    # 判断回文数
    if num_input == num_input[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

# 执行函数
is_palindrome_five_digit()
