car = 'subaru'

# 条件测试1
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # 预测结果：True，实际结果：True，因为car的值确实是'subaru'

# 条件测试2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # 预测结果：False，实际结果：False，因为car的值不是'audi'

# 条件测试3
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # 预测结果：True，实际结果：True，因为car的值不是'audi'

# 条件测试4
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')  # 预测结果：False，实际结果：False，因为car的值是'subaru'

# 条件测试5
print("\nIs car > '奔驰'? I predict False.")  # 假设'奔驰'代表一个汽车品牌
print(car > '奔驰')  # 预测结果：False，实际结果：False，因为'subaru'在字典序上不大于'奔驰'

# 条件测试6
print("\nIs car < '奔驰'? I predict True.")
print(car < '奔驰')  # 预测结果：True，实际结果：True，因为'subaru'在字典序上小于'奔驰'

# 条件测试7
print("\nIs car >= 'subaru'? I predict True.")
print(car >= 'subaru')  # 预测结果：True，实际结果：True，因为car的值等于'subaru'

# 条件测试8
print("\nIs car <= 'subaru'? I predict True.")
print(car <= 'subaru')  # 预测结果：True，实际结果：True，因为car的值等于'subaru'

# 条件测试9
print("\nIs car in ['subaru', 'audi', 'toyota']? I predict True.")
print(car in ['subaru', 'audi', 'toyota'])  # 预测结果：True，实际结果：True，因为'subaru'在列表中

# 条件测试10
print("\nIs car in ['audi', 'toyota', 'honda']? I predict False.")
print(car in ['audi', 'toyota', 'honda'])  # 预测结果：False，实际结果：False，因为'subaru'不在列表中

# 条件测试11
print("\nIs car is not None? I predict True.")
print(car is not None)  # 预测结果：True，实际结果：True，因为car被赋予了一个值，不是None

# 条件测试12
print("\nIs car is an instance of str? I predict True.")
print(isinstance(car, str))  # 预测结果：True，实际结果：True，因为car是一个字符串实例