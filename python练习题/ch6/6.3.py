# 创建一个词汇表，存储编程术语及其含义
programming_terms = {
    'Python': '一种广泛使用的高级编程语言，以其清晰的语法和代码可读性而闻名。',
    'API': '应用程序编程接口，是一组规则和协议，用于构建软件和应用程序。',
    'Variable': '存储数据值的容器，在编程中用于保存信息。',
    'Function': '一段具有特定功能的代码，可以接收输入、处理数据并返回输出。',
    'Loop': '一种控制结构，用于重复执行一段代码直到满足特定条件。'
}

# 以整洁的方式打印每个术语及其含义
for term, definition in programming_terms.items():
    print(f"{term}:")
    print("   " + definition)
    print()  # 打印一个空行以分隔每个术语及其含义