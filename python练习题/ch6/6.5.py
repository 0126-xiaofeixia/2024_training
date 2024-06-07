#河流
# 创建一个字典，存储河流及其流经的国家
rivers_countries = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# 使用循环为每条河流打印一条消息
for river, country in rivers_countries.items():
    print(f"The {river} runs through {country}.")

# 使用循环打印字典中每条河流的名字
print("\nList of rivers:")
for river in rivers_countries:
    print(river)

# 使用循环打印字典包含的每个国家的名字
print("\nList of countries through which the rivers flow:")
for country in rivers_countries.values():
    print(country)