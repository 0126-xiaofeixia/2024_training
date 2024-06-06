#你的披萨 我的披萨
# 原始的披萨列表
my_pizzas = ["pepperoni", "margarita", "hawaiian"]

# 创建披萨列表的副本并赋给变量 friend_pizzas
friend_pizzas = my_pizzas.copy()

# 在原始披萨列表中添加一种披萨
my_pizzas.append("bbq chicken")

# 在 friend_pizzas 列表中添加另一种披萨
friend_pizzas.append("veggie supreme")

# 打印消息并使用 for 循环打印第一个列表
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

# 打印消息并使用 for 循环打印第二个列表
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
