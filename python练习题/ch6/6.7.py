
# 创建第一个表示个人信息的字典
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}


# 创建第二个表示个人信息的字典
person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

# 创建第三个表示个人信息的字典
person3 = {
    'first_name': 'Dave',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}

# 将这三个字典存储在一个名为people的列表中
people = [person1, person2, person3]

# 遍历people列表，打印每个人的所有信息
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")  # 使用\n来开始一个新行