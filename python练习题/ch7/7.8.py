#熟食店
# 创建一个包含各种三明治名字的列表
sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie']

# 创建一个空列表，用于存储完成的三明治
finished_sandwiches = []

# 遍历三明治订单列表
for sandwich in sandwich_orders:
    # 打印制作三明治的消息
    print(f"I made your {sandwich} sandwich.")
    # 将完成的三明治添加到 finished_sandwiches 列表
    finished_sandwiches.append(sandwich)

# 检查所有三明治是否都已制作完毕
if len(finished_sandwiches) == len(sandwich_orders):
    # 打印完成的三明治列表
    print("\nAll sandwiches have been made! Here's the list of sandwiches:")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich)