#宠物
# 创建第一个表示宠物的字典
pet1 = {
    'type': 'Dog',
    'owner': 'Alice'
}

# 创建第二个表示宠物的字典
pet2 = {
    'type': 'Cat',
    'owner': 'Bob'
}

# 创建第三个表示宠物的字典
pet3 = {
    'type': 'Parrot',
    'owner': 'Charlie'
}

# 将这些字典存储在一个名为pets的列表中
pets = [pet1, pet2, pet3]

# 遍历pets列表，打印每个宠物的所有信息
for pet in pets:
    print(f"Pet Type: {pet['type']}")
    print(f"Owner: {pet['owner']}")