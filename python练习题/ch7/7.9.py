#五⾹烟熏⽜⾁卖完了
# 创建一个包含各种三明治名字的列表，确保pastrami至少出现三次
sandwich_orders = ['pastrami', 'tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'veggie']

# 创建一个空列表，用于存储完成的三明治
finished_sandwiches = []

# 打印消息，指出五香烟熏牛肉卖完了
print("Sorry, we are out of pastrami!")

# 使用while循环删除sandwich_orders中的所有pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 遍历sandwich_orders列表制作三明治
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# 确认finished_sandwiches中未包含'pastrami'
if 'pastrami' not in finished_sandwiches:
    print("\nWe have confirmed that 'pastrami' is not included in the finished sandwiches.")