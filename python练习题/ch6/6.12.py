#扩展
# 创建一个包含城市信息的字典，包括国家、人口、一个有趣事实、气候、著名景点等
cities = {
    'New York': {
        'country': 'USA',
        'population': '8,336,817',
        'fact': 'New York is known as the melting pot of cultures.',
        'climate': 'Humid Subtropical',
        'attractions': ['Statue of Liberty', 'Central Park', 'Times Square'],
        'coordinates': (40.7128, -74.0060),
        'language': 'English'
    },
    'Paris': {
        'country': 'France',
        'population': '2,148,271',
        'fact': 'Paris is often called the City of Light.',
        'climate': 'Oceanic',
        'attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
        'coordinates': (48.8566, 2.3522),
        'language': 'French'
    },
    'Beijing': {
        'country': 'China',
        'population': '21,516,000',
        'fact': 'Beijing is famous for its ancient history and rich cultural heritage.',
        'climate': 'Humid Continental',
        'attractions': ['Forbidden City', 'Great Wall', 'Summer Palace'],
        'coordinates': (39.9042, 116.4074),
        'language': 'Mandarin'
    }
}

# 定义一个函数，用于格式化和打印城市信息
def print_city_info(city_name, city_data):
    print(f"City: {city_name}")
    print(f"  Country: {city_data['country']}")
    print(f"  Population: {city_data['population']}")
    print(f"  Climate: {city_data['climate']}")
    print("  Top Attractions:")
    for attraction in city_data['attractions']:
        print(f"    - {attraction}")
    print(f"  Fact: {city_data['fact']}")
    print(f"  Coordinates: ({city_data['coordinates'][0]}, {city_data['coordinates'][1]})")
    print(f"  Language: {city_data['language']}\n")

# 遍历cities字典，使用定义好的函数打印每座城市的详细信息
for city in cities:
    print_city_info(city, cities[city])