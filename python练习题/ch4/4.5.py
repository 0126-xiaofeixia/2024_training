#100 万求和 
import time
# 创建一个包含从1到1,000,000的整数的列表
numbers = list(range(1, 1000001))

# 使用min()函数核实列表的最小值
min_number = min(numbers)
print(f"The minimum number in the list is: {min_number}")

# 使用max()函数核实列表的最大值
max_number = max(numbers)
print(f"The maximum number in the list is: {max_number}")

# 记录当前时间，以便计算sum()函数的执行时间
start_time = time.time()

# 对列表调用sum()函数，计算总和
total_sum = sum(numbers)

# 计算sum()函数的执行时间
end_time = time.time()
execution_time = end_time - start_time

# 打印总和和执行时间
print(f"The sum of the numbers from 1 to 1,000,000 is: {total_sum}")
print(f"The execution time for sum() is: {execution_time} seconds")