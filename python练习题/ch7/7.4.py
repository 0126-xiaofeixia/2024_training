# 初始化一个空列表来存储配料
pizza_toppings = []

# 使用循环来获取用户输入的比萨配料
while True:
    # 提示用户输入一种配料
    topping = input("Please enter a pizza topping or type '!quit!' to finish: ")

    # 检查用户是否输入了退出命令
    if topping == '!quit!':
        break  # 如果是，退出循环

    # 打印消息，指出要在比萨中添加这种配料
    print(f"Adding {topping} to your pizza.")

    # 将配料添加到列表中
    pizza_toppings.append(topping)

# 循环结束后，打印出所有添加的比萨配料
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print(topping)