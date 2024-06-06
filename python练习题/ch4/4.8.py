#立方
# 使用列表推导式创建一个包含前10个整数的立方的列表
cubes = [number ** 3 for number in range(1, 11)]

# 使用 for 循环打印这些立方数
for cube in cubes:
    print(cube)