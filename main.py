n = input()
print("错误提示" if len(n)!=5 or not n.isdigit() else "是回文数" if n==n[::-1] else "不是回文数")
