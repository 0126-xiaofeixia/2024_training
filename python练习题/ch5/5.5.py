# 设置外星人的颜色
#版本1
alien_color = 'green'
#版本2
# alien_color = 'yellow'
# 版本3
# alien_color = 'red'


# 使用 if-elif-else 结构根据外星人的颜色给玩家计分
if alien_color == 'green':
    print("You destroyed a green alien. You earned 5 points.")
elif alien_color == 'yellow':
    print("You destroyed a yellow alien. You earned 10 points.")
else:
    print("You destroyed a red alien. You earned 15 points.")