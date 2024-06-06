#修改嘉宾名单
dinner_guests = ["Albert", "Mariee", "Leonardo"]
print("Albert can not have dinner")
dinner_guests.remove('Albert')
dinner_guests.insert(1,'bob')
# 遍历列表并打印邀请消息
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")