# 创建一个名为cities的字典，其中包含三个城市的信息
cities = {
    'New York': {
        'country': 'USA',
        'population': '8,336,817',
        'fact': 'New York is known as the melting pot of cultures.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '13,929,286',
        'fact': "Tokyo is the world's most populous metropolitan area."
    },
    'London': {
        'country': 'UK',
        'population': '8,787,892',
        'fact': 'London is one of the world\'s leading financial centers.'
    }
}

# 遍历cities字典，打印每座城市的名字及其相关信息
for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")