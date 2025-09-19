def is_palindrome(num):
    # 检查输入是否为5位数字
    if not num.isdigit() or len(num) != 5:
        return "错误：输入必须是5位数字"
    
    # 判断是否为回文数
    if num == num[::-1]:
        return "是回文数"
    else:
        return "不是回文数"

# 从键盘输入一个5位数字
input_num = input("请输入一个5位数字: ")
result = is_palindrome(input_num)
print(result)
