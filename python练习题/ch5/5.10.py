# 创建一个包含5个用户名的列表
current_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# 创建一个包含5个新用户名的列表，其中一些可能与current_users中的用户名重复
new_users = ['alice', 'Frank', 'bob', 'George', 'eve']

# 创建current_users的副本，并转换为全小写版本，以便进行不区分大小写的比较
current_users_lower = [user.lower() for user in current_users]

# 遍历new_users列表，检查每个用户名是否已被使用
for new_user in new_users:
    # 将新用户名转换为小写，以进行比较
    new_user_lower = new_user.lower()
    
    # 检查新用户名（小写形式）是否在current_users_lower中
    if new_user_lower in current_users_lower:
        print(f"You need to pick a different username. '{new_user}' is already in use.")
    else:
        print(f"The username '{new_user}' is available.")