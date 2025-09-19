num = input().strip()
if len(num) != 5 or not num.isdigit():
    print("错误提示")
else:
    print("是回文数" if num == num[::-1] else "不是回文数")
