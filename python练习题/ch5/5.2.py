# 检查两个字符串是否相等和不等
str1 = "hello"
str2 = "world"
print("Is str1 equal to str2? I predict False.")
print(str1 == str2)  # False

print("\nIs str1 not equal to str2? I predict True.")
print(str1 != str2)  # True

# 使用lower()方法的条件测试
str3 = "HELLO"
str4 = "hello"
print("\nDoes str3.lower() equal str4? I predict True.")
print(str3.lower() == str4)  # True

print("\nDoes str3 equal str4 when both are in lower case? I predict True.")
print(str3.lower() == str4.lower())  # True

# 涉及相等、不等、大于、小于、大于等于和小于等于的数值比较
num1 = 10
num2 = 20
print("\nIs num1 equal to num2? I predict False.")
print(num1 == num2)  # False

print("Is num1 greater than num2? I predict False.")
print(num1 > num2)  # False

print("Is num1 less than or equal to num2? I predict True.")
print(num1 <= num2)  # True

# 使用关键字and和or的条件测试
bool1 = True
bool2 = False
print("\nIs bool1 True and bool2 True? I predict False.")
print(bool1 and bool2)  # False

print("Is bool1 True or bool2 True? I predict True.")
print(bool1 or bool2)  # True

# 测试特定的值是否在列表中
values = [1, 2, 3, 4, 5]
print("\nIs 3 in values list? I predict True.")
print(3 in values)  # True

print("Is 6 in values list? I predict False.")
print(6 in values)  # False

# 测试特定的值是否不在列表中
print("\nIs 3 not in values list? I predict False.")
print(3 not in values)  # False

print("Is 6 not in values list? I predict True.")
print(6 not in values)  # True