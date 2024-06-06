#缩短名单
dinner_guests = ["Albert", "Mariee", "Leonardo"]
print("we have found a bigger place")
dinner_guests.insert(0,"xiaolan")
dinner_guests.insert(2,"xiaohong")
dinner_guests.append("xiaoming")

print("only two people")
while len(dinner_guests) > 2:
    guest_to_remove = dinner_guests.pop()
    print(f"Dear {guest_to_remove}, I regret to inform you that I can only invite two guests for dinner.")
# 确认剩余的两位嘉宾
for guest in dinner_guests:
    print(f"Dear {guest}, you are still invited to dinner.")
# 删除最后两位嘉宾，清空名单
del dinner_guests[:]

# 打印空的名单，确认程序结束时名单是空的
print("The dinner guest list is now:", dinner_guests)