# 创建一个包含用户名的列表，可以包含 'admin' 用户
usernames = ['jaden', 'sarah', 'admin', 'mike', 'julia']

# 检查用户名列表是否为空
if not usernames:  # 如果列表为空
    print("We need to find some users!")
else:
    # 遍历用户名列表
    for username in usernames:
        # 检查用户名是否为 'admin'
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            # 打印普通问候消息
            print(f"Hello {username.title()}, thank you for logging in again.")

# 删除列表中的所有用户名
usernames.clear()

# 再次检查用户名列表是否为空，并打印相应的消息
if not usernames:
    print("We need to find some users!")