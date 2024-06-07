# 创建一个包含用户名的列表，其中包含 'admin' 用户
usernames = ['jaden', 'sarah', 'admin', 'mike', 'julia']

# 遍历用户名列表
for username in usernames:
    # 检查用户名是否为 'admin'
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        # 打印普通问候消息，使用 title() 方法使用户名首字母大写
        print(f"Hello {username.title()}, thank you for logging in again.")