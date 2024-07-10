# 示例对象
class MyClass:
    def __init__(self):
        self.x = 10

    def my_method(self):
        print("Hello, I'm a method!")

# 创建实例对象
obj = MyClass()

# 调用实例属性
print(obj.x)

# 调用实例方法
obj.my_method()

# 使用dir()函数
print(dir(obj))