#自助餐
# 定义一个包含5种简单食品的元组
simple_foods = ("soup", "salad", "sandwich", "pizza", "ice cream")

# 使用 for 循环打印该餐馆提供的5种食品
print("The self-service restaurant offers the following foods:")
for food in simple_foods:
    print(food)

# 尝试修改元组中的一个元素，这将引发 TypeError
try:
    simple_foods[1] = "spaghetti"  # 尝试修改第二个元素
except TypeError as e:
    print("Error:", e)
# 餐馆调整菜单，替换了两种食品
new_foods = ("soup", "pasta", "sandwich", "tacos", "ice cream")

# 使用 for 循环打印新元组中的每个元素
print("\nAfter menu adjustment, the self-service restaurant now offers:")
for food in new_foods:
    print(food)