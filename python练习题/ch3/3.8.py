#放眼世界
# 定义一个包含旅游地点的列表，元素不是按字母顺序排列的
travel_destinations = ["Paris", "New York", "Tokyo", "Cairo", "Sydney"]

# 按原始排列顺序打印该列表
print("原始列表:", travel_destinations)

# 使用 sorted() 按字母顺序打印这个列表，不修改原列表
print("按字母顺序排序（不修改原列表）:", sorted(travel_destinations))

# 再次打印原始列表，核实排列顺序未变
print("原始列表（未变）:", travel_destinations)

# 使用 sorted() 按与字母顺序相反的顺序打印这个列表，不修改原列表
print("按字母逆序排序（不修改原列表）:", sorted(travel_destinations, reverse=True))

# 再次打印原始列表，核实排列顺序未变
print("原始列表（未变）:", travel_destinations)

# 使用 reverse() 修改列表元素的排列顺序
travel_destinations.reverse()
print("使用 reverse() 修改后的列表:", travel_destinations)

# 再次使用 reverse() 恢复到原来的排列顺序
travel_destinations.reverse()
print("再次使用 reverse() 后的列表（恢复原状）:", travel_destinations)

# 使用 sort() 修改该列表，使其元素按字母顺序排列
travel_destinations.sort()
print("使用 sort() 按字母顺序排序后的列表:", travel_destinations)

# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列
travel_destinations.sort(reverse=True)
print("使用 sort() 按字母逆序排序后的列表:", travel_destinations)