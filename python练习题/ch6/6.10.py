# 创建一个字典，存储每个人喜欢的多个数字
favorite_numbers = {
    'Alice': [7, 23, 45],
    'Bob': [13, 29],
    'Charlie': [42, 56, 77, 89],
    'Diana': [19, 31, 67],
    'Evan': [23, 47, 53]
}

# 遍历favorite_numbers字典，打印每个人的名字及其喜欢的数字
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"  - {number}")