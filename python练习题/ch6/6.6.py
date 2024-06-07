favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    } 
# 创建一个包含一些人的名单，他们可能已经或还未参与调查
survey_list = ['jen', 'sarah', 'Charlie', 'David', 'Eve']

# 遍历名单
for person in survey_list:
    if person in favorite_languages:
        # 如果这个人已经在字典中，打印感谢消息
        print(f"Thank you, {person}, for participating in the survey!")
    else:
        # 如果这个人还未参与调查，打印邀请消息
        print(f"Hi {person}, would you like to participate in our favorite programming language survey?")