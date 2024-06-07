#喜欢的地方
# 创建一个名为favorite_places的字典，存储三个人喜欢的1~3个地方
favorite_places = {
    'Alice': ['Beach', 'Mountains', 'City Park'],
    'Bob': ['Library', 'Museum'],
    'Charlie': ['Forest', 'Lake']
}

# 遍历favorite_places字典，打印每个人的名字及其喜欢的地方
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"  - {place}")