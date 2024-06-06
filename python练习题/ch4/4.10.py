#切片
# 使用列表推导式生成前10个整数的立方的列表
cubes = [x**3 for x in range(1, 11)]

# 打印前三个元素
print("The first three items in the list are:")
print(cubes[:3])  # 使用切片来获取列表的前三个元素

# 假设列表长度足够，打印中间的三个元素
# 这里我们简单地取中间位置的三个数，即第4、5、6个元素
print("Three items from the middle of the list are:")
print(cubes[3:6])  # 使用切片来获取列表中间的三个元素

# 打印末尾的三个元素
print("The last three items in the list are:")
print(cubes[-3:])  # 使用切片来获取列表末尾的三个元素