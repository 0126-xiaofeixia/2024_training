# 请求用户输入一个数
number = int(input("Please enter a number: "))

# 检查这个数是否是10的整数倍
if number % 10 == 0:
    print("Yes, the number is a multiple of 10.")
else:
    print("No, the number is not a multiple of 10.")