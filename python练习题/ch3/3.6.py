dinner_guests = ["Albert", "Mariee", "Leonardo"]
print("we have found a bigger place")
dinner_guests.insert(0,"xiaolan")
dinner_guests.insert(2,"xiaohong")
dinner_guests.append("xiaoming")
# 遍历列表并打印邀请消息
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")