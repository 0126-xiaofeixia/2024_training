# 初始化active变量为True，表示循环处于活跃状态
active = True

# 使用循环来询问用户的年龄并给出票价
while active:
    # 请求用户输入年龄
    age = input("Please enter your age or type 'quit!' to exit: ")

    # 检查用户是否输入了退出命令
    if age.lower() == 'quit!':
        print("Exiting the ticket pricing program.")
        active = False  # 设置active为False，将退出循环
        break  # 使用break语句确保立即退出循环

    try:
        # 尝试将输入的年龄转换为整数
        age = int(age)
    except ValueError:
        # 如果转换失败，提示用户输入有效的年龄，并继续循环
        print("Please enter a valid number for age or 'quit!' to exit.")
        continue

    # 根据年龄给出票价
    if age < 3:
        print("Admission for you is free!")
    elif age <= 12:
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $15.")

# 循环结束后，打印感谢消息
print("Thank you for using the movie ticket pricing program.")