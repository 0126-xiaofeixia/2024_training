#⽂件扩展名 Python 提供了removesuffix() ⽅法，其⼯作原理与 removeprefix() 很像。请将值 'python_notes.txt'赋给变量 filename，再使⽤ removesuffix() ⽅法来显⽰不包含扩展名的⽂件名，就像⽂件浏览器所做的那样
filename = "python_notes.txt"
filename_without_suffix = filename.removesuffix('.txt')
# 打印结果
print("不包含扩展名的文件名是:", filename_without_suffix)
