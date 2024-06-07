#喜欢的数
# 创建一个字典，存储5个人喜欢的数
favorite_numbers = {
    'Alice': 7,
    'Bob': 13,
    'Charlie': 42,
    'Diana': 19,
    'Evan': 23
}

# 遍历字典，打印每个人的名字和喜欢的数
for name, favorite_number in favorite_numbers.items():
    print(f"{name}'s favorite number is {favorite_number}.")