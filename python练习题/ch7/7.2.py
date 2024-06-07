# 请求用户输入用餐人数
number_of_people = int(input("Please enter the number of people in your dining party: "))

# 检查用餐人数是否超过8人
if number_of_people > 8:
    print("I'm sorry, we do not have a table available for your group.")
else:
    print("We have a table available for your group.")