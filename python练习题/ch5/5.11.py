#序数
# 创建一个包含数字1到9的列表
numbers = list(range(1, 10))

# 遍历这个列表
for number in numbers:
    # 使用 if-elif-else 结构打印每个数字对应的序数
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        # 对于其他数字，简单地添加 "th" 后缀
        print(f"{number}th")